// CUDA include files
#include <cuda_runtime.h>

// CMSSW include files
#include "HeterogeneousCore/CUDAUtilities/interface/cudaCheck.h"
#include "RecoVertex/PrimaryVertexProducer/interface/clusterizerCUDA.h"
#include <stdio.h>
namespace clusterizerCUDA {

  __global__ void kernel_calc_exp_arg_range(double beta,
                                          double track_z,
                                          double botrack_dz2,
                                          double* zvtx,
                                          double* expvtx,
                                          const unsigned int kmin,
                                          const unsigned int kmax){
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x + kmin;
    size_t gridSize = blockDim.x * gridDim.x;
    for (unsigned int ivertex = firstElement; ivertex < kmax; ivertex += gridSize) {
      double mult_res = track_z - zvtx[ivertex];
      expvtx[ivertex] = botrack_dz2 * (mult_res * mult_res);
    }
  }

  __global__ void kernel_track_loop(unsigned int nt, unsigned int nv, double beta, bool updateTc, double rho0, double osumtkwt, double Z_init, const unsigned int * tkmin, const unsigned int * tkmax, double * tz, double * tdz2, double * twgt, double * vrho, double * vz, double * tsumz, double * vsw, double * vswe, double* tvsw, double* tvse, double* tvswz, double* tvswE, double* tvexp, double* tvexparg, double* delta){
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x; // This is going to be the track index
    size_t gridSize = blockDim.x * gridDim.x;
    // Initiliaze stuff to 0
    for (unsigned int itrack = firstElement; itrack < nt ; itrack += gridSize){
      for (unsigned int ivertex = 0 ; ivertex < nv ; ++ivertex){ 
        tvsw[ivertex*nt + itrack]     = 0;
        tvse[ivertex*nt + itrack]     = 0;
        tvswz[ivertex*nt + itrack]    = 0;
        tvswE[ivertex*nt + itrack]    = 0;
        tvexp[ivertex*nt + itrack]    = 0;
        tvexparg[ivertex*nt + itrack] = 0;
      }
    }

    for (unsigned int itrack = firstElement; itrack < nt ; itrack += gridSize){
      // First, update vertex stuff
      double botrack_dz2 = -beta * tdz2[itrack];
      tsumz[itrack] = Z_init;
      for (unsigned int ivertex = tkmin[itrack] ; ivertex < tkmax[itrack] ; ++ivertex){
        double mult_res = tz[itrack] - vz[ivertex];
        tvexparg[ivertex*nt + itrack] = botrack_dz2* (mult_res * mult_res);
        tvexp[ivertex*nt + itrack]    = exp(tvexparg[ivertex*nt + itrack]); // exp is defined as device function in cuda 
        tsumz[itrack] += vrho[ivertex]*tvexp[ivertex*nt + itrack];
      }
      if(not(std::isfinite(tsumz[itrack]))) tsumz[itrack] = 0;
      if(tsumz[itrack] > 0){
        double sumw = twgt[itrack]/tsumz[itrack];
        if (updateTc){
          for (unsigned int ivertex = tkmin[itrack] ; ivertex < tkmax[itrack] ; ++ivertex){
            tvse[ivertex*nt + itrack]  = tvexp[ivertex*nt + itrack] * sumw;
            double w                   = vrho[ivertex] * tvexp[ivertex*nt + itrack] * sumw * tdz2[itrack];
            tvsw[ivertex*nt + itrack]  = w;
            tvswz[ivertex*nt + itrack] = w * tz[itrack];
            tvswE[ivertex*nt + itrack] = w * tvexparg[ivertex*nt + itrack]/ beta;
          }
        }
        else{
          for (unsigned int ivertex = tkmin[itrack] ; ivertex < tkmax[itrack] ; ++ivertex){
            tvse[ivertex*nt + itrack]  = tvexp[ivertex*nt + itrack] * sumw;
            double w                   = vrho[ivertex] * tvexp[ivertex*nt + itrack] * sumw * tdz2[itrack];
            tvsw[ivertex*nt + itrack]  = w;
            tvswz[ivertex*nt + itrack] = w * tz[itrack];
          }
        }
      }
    }
    __syncthreads(); // Need to synchronize, as now we have to add across vertexes
    for (unsigned int ivertex = firstElement; ivertex < nv ; ivertex+=gridSize){
      for (unsigned int itrack = 1 ; itrack < nt ; ++itrack){
        tvse[ivertex*nt] += tvse[ivertex*nt + itrack];
        tvsw[ivertex*nt] += tvsw[ivertex*nt + itrack];
        tvswz[ivertex*nt] += tvswz[ivertex*nt + itrack];
        tvswE[ivertex*nt] += tvswE[ivertex*nt + itrack];
      }
      vsw[ivertex]  = tvsw[ivertex*nt];
      vswe[ivertex] = tvswE[ivertex*nt];
      if (vsw[ivertex] > 0){
        double znew    = tvswz[ivertex*nt]/vsw[ivertex];
        delta[ivertex] = std::abs(znew-vz[ivertex]);
        vz[ivertex]    = znew; 
      }
      vrho[ivertex]    = vrho[ivertex] * tvse[ivertex*nt] * osumtkwt; 
    }
    
  }

#ifdef __CUDACC__

  void kernel_update_wrapper(unsigned int nt, unsigned int nv, double beta, bool updateTc, double rho0, double osumtkwt, double Z_init, const unsigned int * tkmin, const unsigned int * tkmax, double * tz, double * tdz2, double * twgt, double * vrho, double * vz, double * tsumz, double * vsw, double * vswe, double * delta, cudaStream_t stream){

    int blockSize = 64; // This should be optimized with some care
    int gridSize     = (nt + blockSize -1)/blockSize; // Together with this
    // Reserve the internal matrices for use inside device only
    auto tvsw_gpu    = cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    auto tvse_gpu    = cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    auto tvswz_gpu   = cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    auto tvswE_gpu   = cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    auto tvexp_gpu   = cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    auto tvexparg_gpu= cms::cuda::make_device_unique<double[]>(nt*nv, cudaStreamDefault);
    // Launch kernel
    kernel_track_loop<<<gridSize, blockSize, 0, stream>>>(nt, nv, beta, updateTc, rho0, osumtkwt, Z_init, tkmin, tkmax, tz, tdz2, twgt, vrho, vz, tsumz, vsw, vswe, tvsw_gpu.get(), tvse_gpu.get(), tvswz_gpu.get(), tvswE_gpu.get(), tvexp_gpu.get(), tvexparg_gpu.get(), delta);
    cudaCheck(cudaGetLastError());
  } 

#endif
}
