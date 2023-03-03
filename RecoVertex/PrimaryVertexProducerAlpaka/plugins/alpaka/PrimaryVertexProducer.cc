#include "DataFormats/PortableVertex/interface/alpaka/VertexDeviceCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/stream/EDProducer.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/EDPutToken.h"
#include "HeterogeneousCore/AlpakaCore/interface/alpaka/ESGetToken.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

#include "TestAlgo.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {
  /**
   * This class demonstrates a stream EDProducer that
   * - consumes a host EDProduct
   * - produces a device EDProduct (that can get transferred to host automatically)
   */
  class PrimaryVertexProducer : public stream::EDProducer<> {
  public:
    PrimaryVertexProducer(edm::ParameterSet const& config) {
      tracksToken_ = consumes(config.getParameter<edm::InputTag>("tracks")); //TODO:: move from auto to proper dataformat explicitly
      devicePutToken_ = produces(); //TODO:: move from auto to proper dataformat explicitly
    }

    void produce(device::Event& iEvent, device::EventSetup const& iSetup) override {
      auto inputTracks = iEvent.getHandle(tracksToken_); // We read the reco::Tracks
      auto deviceProduct = std::make_unique<portablevertex::VertexDeviceCollection>(size_, alpaka::getDev(iEvent.queue())); //We produce portable vertex

      // Currently dummy, this will be the producer
      algo_.fill(iEvent.queue(), *deviceProduct);

      iEvent.put(devicePutToken_, std::move(deviceProduct));
    }

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
      edm::ParameterSetDescription desc;
      desc.add<edm::InputTag>("tracks");

      edm::ParameterSetDescription psetSize;
      psetSize.add<int32_t>("alpaka_serial_sync");
      psetSize.add<int32_t>("alpaka_cuda_async");
      desc.add("size", psetSize);
      descriptions.addWithDefaultLabel(desc);
    }

  private:
    edm::EDGetTokenT<reco::Track> tracksToken_;
    device::EDPutToken<portabletest::VertexDeviceCollection> devicePutToken_;
    const int32_t size_;

    // implementation of the algorithm
    TestAlgo algo_; // TODO:: make this do something
  };

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#include "HeterogeneousCore/AlpakaCore/interface/MakerMacros.h"
DEFINE_FWK_ALPAKA_MODULE(PrimaryVertexProducer);
