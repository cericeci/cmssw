#ifndef testRadixGPU_h
#define testRadixGPU_h
#include <cstddef>
#include <cstdint>
#include "HeterogeneousCore/CUDAUtilities/interface/cudaCheck.h"
#include "HeterogeneousCore/CUDAUtilities/interface/radixSort.h"



namespace testRadixGPU{
  void testWrapper(double * gpu_input, int * gpu_product, int elements); 
}

#endif
