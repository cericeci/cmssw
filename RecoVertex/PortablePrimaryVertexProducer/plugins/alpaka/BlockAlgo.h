#ifndef RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_BlockAlgo_h
#define RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_BlockAlgo_h

#include "DataFormats/VertexSoA/interface/alpaka/TrackForVertexDeviceCollection.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  class BlockAlgo {
  public:
    BlockAlgo();
    void createBlocks(Queue& queue,
                      const TrackForVertexDeviceCollection& inputTrack,
                      TrackForVertexDeviceCollection& trackInBlocks,
                      int32_t blockSize,
                      double blockOverlap);  // The actual block creation

  private:
  };

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#endif  // RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_BlockAlgo_h
