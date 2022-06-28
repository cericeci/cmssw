#include "testRadixGPU.h"


namespace testRadixGPU{
__global__ void testKernel(double * gpu_input, int * gpu_product, int elements){
      size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x; // This is going to be the track index
      size_t gridSize = blockDim.x * gridDim.x;

      __shared__ __restrict__ uint16_t order[512];
      __shared__ uint16_t sws[512];
      __shared__ float   z[512];

      for (unsigned int itrack=firstElement; itrack<elements; itrack+=gridSize) {
        z[itrack] = gpu_input[itrack];
      }

      __syncthreads();
      radixSort<float, 2>(z, order, sws, elements);
      if (threadIdx.x == 0 && blockIdx.x == 0) {
            for (unsigned int itrackO=0; itrackO < elements; itrackO++){
                int itrack = order[itrackO];
                printf("Radix sort: At position %i, old track position %i with z at input %f , z sorted %f\n", itrackO, itrack, gpu_input[itrack], z[itrack]);
                gpu_product[itrackO] = itrack;
            }
       }
       __syncthreads();
       /*__shared__ uint16_t sortInd[4096];
       if (threadIdx.x == 0 && blockIdx.x == 0){
       for (uint16_t i = 0; i < elements; ++i){
         sortInd[i] = i;
       }
       std::sort(sortInd, sortInd + elements, [&](auto i, auto j) { return z[i] < z[j]; });
            for (unsigned int itrackO=0; itrackO < elements; itrackO++){
                int itrack = order[itrackO];
                printf("std::sort: At position %i, old track position %i with z %f\n", itrackO, itrack, gpu_input[itrack]);
            }
       }*/
}


void testWrapper(double * gpu_input, int * gpu_product, int elements){
    auto blockSize = 512;                                // somewhat arbitrary
    auto gridSize  =   1;  // round up to cover the sample size
    testKernel<<<gridSize, blockSize>>>(gpu_input, gpu_product, elements);
    cudaCheck(cudaGetLastError());
}
}
