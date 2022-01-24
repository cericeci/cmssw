// CUDA include files
#include <cuda_runtime.h>

// CMSSW include files
#include "HeterogeneousCore/CUDAUtilities/interface/cudaCheck.h"
#include "RecoVertex/PrimaryVertexProducer/interface/clusterizerCUDA.h"
#include <stdio.h>
namespace clusterizerCUDA {

  __global__ void kernel_calc_exp_arg_range(float beta,
                                          double track_z,
                                          double botrack_dz2,
                                          vertex_t* vertices,
                                          const unsigned int kmin,
                                          const unsigned int kmax){
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x + kmin;
    size_t gridSize = blockDim.x * gridDim.x;
    for (unsigned int ivertex = firstElement; ivertex < kmax; ivertex += gridSize) {
      double mult_res = track_z - vertices->zvtx[ivertex];
      vertices->exp_arg[ivertex] = botrack_dz2 * (mult_res * mult_res);
    }
  }

  __global__ void kernel_calc_normalization_range = (float o_trk_sum_Z, float o_trk_dz2, float tmp_trk_z, vertex_t* gpuvertices, const unsigned int kmin, const unsigned int kmax, bool updateTc, cudaStream_t cudaStreamDefault) {
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x + kmin;
    size_t gridSize = blockDim.x * gridDim.x;
    // auto-vectorized
    if (updateTc) {
      for (unsigned int k = firstElement; k < kmax; k += gridSize) {
        vertices->se[k] += vertices->exp[k] * o_trk_sum_Z;
        auto w = vertices->rho[k] * vertices->exp[k] * (o_trk_sum_Z * o_trk_dz2);
        vertices->sw[k] += w;
        vertices->swz[k] += w * tmp_trk_z;
        vertices->swE[k] += w * vertices->exp_arg[k];
      }
    } else {
      // same loop but without updating sWE if we are not changing T_c
      for (unsigned int k = kmin; k < kmax; ++k) {
        vertices->se[k] += vertices->exp[k] * o_trk_sum_Z;
        auto w = vertices->rho[k] * vertices->exp[k] * (o_trk_sum_Z * o_trk_dz2);
        vertices->sw[k] += w;
        vertices->swz[k] += w * tmp_trk_z;
      }
    }
  }
  
  __global__ void kernel_calc_z(float osumtkwt, int nv, vertex_t* gpuvertices, double * delta_gpu){
    size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x;
    size_t gridSize = blockDim.x * gridDim.x;
    for (unsigned int ivertex = firstElement; ivertex < nv; ivertex += gridSize) {
      if (vertices->sw[ivertex] > 0) {
        auto znew = vertices->swz[ivertex] / vertices->sw[ivertex];
        delta_gpu[ivertex] = std::abs(vertices->zvtx[ivertex] - znew); //Modify slightly the CPU code to allow concurrently running this
        vertices->zvtx[ivertex] = znew;
      }
    }
  }

#ifdef __CUDACC__
  // Only on GPUs, of course...
  void kernel_calc_exp_arg_range_wrapper(float beta, double track_z, double botrack_dz2, vertex_t* vertices, const unsigned int kmin, const unsigned int kmax, cudaStream_t stream){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (kmax - kmin + blockSize - 1)/blockSize; //Vertices only update in the kmin--kmax range for the given track 
    kernel_calc_exp_arg_range<<<gridSize, blockSize, 0, stream>>>(beta, track_z, botrack_dz2, vertices, kmin, kmax);
    cudaCheck(cudaGetLastError());
  }

  void kernel_calc_normalization_wrapper(float o_trk_sum_Z, float o_trk_dz2, float tmp_trk_z, vertex_t* gpuvertices, const unsigned int kmin, const unsigned int kmax, bool updateTc, cudaStream_t cudaStreamDefault){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (kmax - kmin + blockSize - 1)/blockSize; //Vertices only update in the kmin--kmax range for the given track
    kernel_calc_exp_arg_range<<<gridSize, blockSize, 0, stream>>>(o_trk_sum_Z, o_trk_dz2, tmp_trk_z, gpuvertices, kmin, kmax, updateTc);
    cudaCheck(cudaGetLastError());
  }

  void kernel_calc_z_wrapper(float osumtkwt, int nv, vertex_t* gpuvertices, double * delta_gpu, cudaStream_t cudaStreamDefault){
    int blockSize = 32; // This should be optimized with some care
    int gridSize  = (blockSize - 1)/blockSize; //Here, loop everything
    kernel_calc_z<<<gridSize, blockSize, 0, stream>>>(osumtkwt, nv, gpuvertices, delta_gpu);
    cudaCheck(cudaGetLastError());
  }
#endif
}
