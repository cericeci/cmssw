#ifndef trackFilterCUDA_h
#define trackFilterCUDA_h
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include <cstddef>
#include <cstdint>
#include "CUDADataFormats/Vertex/interface/ZVertexHeterogeneous.h"

namespace trackFilterCUDA {
  void filterWrapper(reco::TransientTrack const* itk, bool* obool, int size);
  /* How do we do this in a simpler way??
    struct configParams {
    float maxD0Sig_;
    float maxD=Error_;
    float maxDzError_;
    float minPt_;
    float maxEta_;
    float maxNormChi2_;
    int minPxLayers_;
    int minSiLayers_;
    int quality_;
  }*/
}

#endif
