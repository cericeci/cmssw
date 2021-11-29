// CUDA include files
#include <cuda_runtime.h>

// CMSSW include files
#include "HeterogeneousCore/CUDAUtilities/interface/cudaCheck.h"
#include "trackFilterCUDA.h"

namespace trackFilterCUDA {

  __host__ __device__ inline void filter(reco::TransientTrack const& tk, bool& b){
    b = false;
    if ( (tk.stateAtBeamLine().transverseImpactParameter().significance() < 12.0) && (tk.stateAtBeamLine().transverseImpactParameter().error() < 1.0) && (tk.track().dzError() < 1.0)){
      if (tk.impactPointState().globalMomentum().transverse() > 0.0){
        if (std::fabs(tk.impactPointState().globalMomentum().eta()) < 4.0){
          if (tk.normalizedChi2() < 10){
            if (tk.hitPattern().pixelLayersWithMeasurement() >= 1 && tk.hitPattern().trackerLayersWithMeasurement() >= 0){
              b = true;
            }
          }
        }  
      }
    }
  }

  __global__ void filterKernel(reco::TransientTrack const* itk, bool* obool, int size){
    int firstElement = threadIdx.x + blockIdx.x * blockDim.x;
    int gridSize = blockDim.x * gridDim.x;
    for (int i = firstElement; i < size; i += gridSize) {
      filter(itk[i], obool[i]);
    }  
  }
 
  void filterWrapper(reco::TransientTrack const* itk, bool* obool, int size){
    int blockSize = 512;
    int gridSize  = (size + blockSize - 1)/blockSize;
    filterKernel<<<gridSize, blockSize>>>(itk, obool, size);
    cudaCheck(cudaGetLastError());
  }
}
