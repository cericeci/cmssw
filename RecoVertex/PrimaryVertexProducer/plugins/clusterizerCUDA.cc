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

  __global__ void kernel_calc_normalization_range(double o_trk_sum_Z, double o_trk_dz2, double tmp_trk_z, double* expvtx_gpu, double* expargvtx_gpu, double* rhovtx_gpu, double* sevtx_gpu, double* swvtx_gpu, double* swzvtx_gpu, double* swEvtx_gpu, const unsigned int kmin, const unsigned int kmax, bool updateTc) {
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x + kmin;
    size_t gridSize = blockDim.x * gridDim.x;
    // auto-vectorized
    if (updateTc) {
      for (unsigned int k = firstElement; k < kmax; k += gridSize) {
        sevtx_gpu[k] += expvtx_gpu[k] * o_trk_sum_Z;
        auto w = rhovtx_gpu[k] * expvtx_gpu[k] * (o_trk_sum_Z * o_trk_dz2);
        swvtx_gpu[k] += w;
        swzvtx_gpu[k] += w * tmp_trk_z;
        swEvtx_gpu[k] += w * expargvtx_gpu[k];
      }
    } else {
      // same loop but without updating sWE if we are not changing T_c
      for (unsigned int k = firstElement; k < kmax; k += gridSize) {
        sevtx_gpu[k] += expvtx_gpu[k] * o_trk_sum_Z;
        auto w = rhovtx_gpu[k] * expvtx_gpu[k] * (o_trk_sum_Z * o_trk_dz2);
        swvtx_gpu[k] += w;
        swzvtx_gpu[k] += w * tmp_trk_z;
      }
    }
  }
  
  __global__ void kernel_calc_z(double osumtkwt, int nv, vertex_t* vertices, double * delta_gpu){
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x;
    size_t gridSize = blockDim.x * gridDim.x;
    for (int ivertex = firstElement; ivertex < nv; ivertex += gridSize) {
      if (vertices->sw[ivertex] > 0) {
        auto znew = vertices->swz[ivertex] / vertices->sw[ivertex];
        delta_gpu[ivertex] = std::abs(vertices->zvtx[ivertex] - znew); //Modify slightly the CPU code to allow concurrently running this
        vertices->zvtx[ivertex] = znew;
      }
    }
  }

#ifdef __CUDACC__
  // Only on GPUs, of course...
  void kernel_calc_exp_arg_range_wrapper(double beta, double track_z, double botrack_dz2, double* zvtx , double* expvtx, const unsigned int kmin, const unsigned int kmax, cudaStream_t stream){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (kmax - kmin + blockSize - 1)/blockSize; //Vertices only update in the kmin--kmax range for the given track 
    kernel_calc_exp_arg_range<<<gridSize, blockSize, 0, stream>>>(beta, track_z, botrack_dz2, zvtx, expvtx, kmin, kmax);
    cudaCheck(cudaGetLastError());
  }

  void kernel_calc_normalization_wrapper(double o_trk_sum_Z, double o_trk_dz2, double tmp_trk_z, double* expvtx_gpu, double* expargvtx_gpu, double* rhovtx_gpu, double* sevtx_gpu, double* swvtx_gpu, double* swzvtx_gpu, double* swEvtx_gpu, const unsigned int kmin, const unsigned int kmax, bool updateTc, cudaStream_t stream){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (kmax - kmin + blockSize - 1)/blockSize; //Vertices only update in the kmin--kmax range for the given track
    kernel_calc_normalization_range<<<gridSize, blockSize, 0, stream>>>(o_trk_sum_Z, o_trk_dz2, tmp_trk_z, expvtx_gpu, expargvtx_gpu, rhovtx_gpu, sevtx_gpu, swvtx_gpu, swzvtx_gpu, swEvtx_gpu, kmin, kmax, updateTc);
    cudaCheck(cudaGetLastError());
  }

  void kernel_calc_z_wrapper(double osumtkwt, int nv, vertex_t* gpuvertices, double * delta_gpu, cudaStream_t stream){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (blockSize - 1)/blockSize; //Here, loop everything
    kernel_calc_z<<<gridSize, blockSize, 0, stream>>>(osumtkwt, nv, gpuvertices, delta_gpu);
    cudaCheck(cudaGetLastError());
  }
#endif
}
