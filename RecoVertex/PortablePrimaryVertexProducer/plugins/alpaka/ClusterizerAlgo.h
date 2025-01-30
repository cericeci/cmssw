#ifndef RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_ClusterizerAlgo_h
#define RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_ClusterizerAlgo_h

#include "DataFormats/VertexSoA/interface/alpaka/VertexDeviceCollection.h"
#include "DataFormats/VertexSoA/interface/alpaka/TrackForVertexDeviceCollection.h"
#include "RecoVertex/PortablePrimaryVertexProducer/interface/alpaka/ClusterParamsDeviceCollection.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  struct clusterParameters {
    double Tmin;
    double Tpurge;
    double Tstop;
    double vertexSize;
    double coolingFactor;
    double d0CutOff;
    double dzCutOff;
    double uniquetrkweight;
    double uniquetrkminp;
    double zmerge;
    double sel_zrange;
    int32_t convergence_mode;
    double delta_lowT;
    double delta_highT;
  };

  class ClusterizerAlgo {
  public:
    ClusterizerAlgo(Queue& queue, int32_t bSize);

    void clusterize(Queue& queue,
                    TrackForVertexDeviceCollection& inputTracks,
                    VertexDeviceCollection& deviceVertex,
                    const std::shared_ptr<ClusterParamsHostCollection> cParams,
                    int32_t nBlocks,
                    int32_t blockSize);  // Clusterization

    void resplit_tracks(Queue& queue,
                        TrackForVertexDeviceCollection& inputTracks,
                        VertexDeviceCollection& deviceVertex,
                        const std::shared_ptr<ClusterParamsHostCollection> cParams,
                        int32_t nBlocks,
                        int32_t blockSize);  // Clusterization

    void reject_outliers(Queue& queue,
                         TrackForVertexDeviceCollection& inputTracks,
                         VertexDeviceCollection& deviceVertex,
                         const std::shared_ptr<ClusterParamsHostCollection> cParams,
                         int32_t nBlocks,
                         int32_t blockSize);  // Clusterization
    void arbitrate(Queue& queue,
                   TrackForVertexDeviceCollection& inputTracks,
                   VertexDeviceCollection& deviceVertex,
                   const std::shared_ptr<ClusterParamsHostCollection> cParams,
                   int32_t nBlocks,
                   int32_t blockSize);  // Arbitration

  private:
    cms::alpakatools::device_buffer<Device, double[]> beta_;
    cms::alpakatools::device_buffer<Device, double[]> osumtkwt_;
  };

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#endif  // RecoVertex_PortablePrimaryVertexProducer_plugins_alpaka_ClusterizerAlgo_h
