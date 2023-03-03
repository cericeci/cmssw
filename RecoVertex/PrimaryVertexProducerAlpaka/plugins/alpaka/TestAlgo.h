#ifndef RecoVertex_PrimaryVertexProducerAlpaka_plugins_alpaka_TestAlgo_h
#define RecoVertex_PrimaryVertexProducerAlpaka_plugins_alpaka_TestAlgo_h

#include "DataFormats/PortableVertex/interface/alpaka/VertexDeviceCollection.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  class TestAlgo {
  public:
    void fill(Queue& queue, portablevertex::VertexDeviceCollection& vertices, portablevertex::TrackDeviceCollection& tracks ) const;
  };

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#endif  // RecoVertex_PrimaryVertexProducerAlpaka_plugins_alpaka_TestAlgo_h
