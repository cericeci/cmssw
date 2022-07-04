#include "testRadixGPU.h"
#include <thrust/sort.h>
#include <thrust/device_ptr.h>
#include <thrust/execution_policy.h>

namespace testRadixGPU{
__global__ void testKernel(double * gpu_input, int * gpu_product, int elements){
      size_t firstElement = threadIdx.x + blockIdx.x * blockDim.x; // This is going to be the track index
      size_t gridSize = blockDim.x * gridDim.x;

      __shared__ uint16_t order[512];
      __shared__ uint16_t sws[512];
      __shared__ float   z[512];
      for (unsigned int itrack=firstElement; itrack<elements; itrack+=gridSize) {
        z[itrack] = gpu_input[itrack];
        order[itrack] = itrack;
      }
      __syncthreads();
      radixSort<float, 2>(z, order, sws, elements);
      if (threadIdx.x == 0 && blockIdx.x == 0) {
            for (unsigned int itrackO=0; itrackO < elements; itrackO++){
                int itrack = order[itrackO];
                printf("Radix sort with %i elements: At position %i, track position at input %i with z at input %f, z fed to radixSort %f\n", elements, itrackO, itrack, gpu_input[itrack], z[itrack]);
                gpu_product[itrackO] = itrack;
            }
       }
       __syncthreads();
}


void testWrapper(double * gpu_input, int * gpu_product, int elements){
    auto blockSize =   512;                                // somewhat arbitrary
    auto gridSize  =   1;  // round up to cover the sample size
    testKernel<<<gridSize, blockSize>>>(gpu_input, gpu_product, elements);
    cudaCheck(cudaGetLastError());
}
}
