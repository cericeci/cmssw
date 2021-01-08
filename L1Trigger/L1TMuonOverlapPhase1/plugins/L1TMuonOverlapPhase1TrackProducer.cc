#include "L1Trigger/L1TMuonOverlapPhase1/plugins/L1TMuonOverlapPhase1TrackProducer.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ProductRegistryHelper.h"
#include "FWCore/PluginManager/interface/PluginFactory.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticleFwd.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"

#include <algorithm>
#include <iostream>
#include <memory>

L1TMuonOverlapPhase1TrackProducer::L1TMuonOverlapPhase1TrackProducer(const edm::ParameterSet& edmParameterSet)
    : muStubsInputTokens(
          {consumes<L1MuDTChambPhContainer>(edmParameterSet.getParameter<edm::InputTag>("srcDTPh")),
           consumes<L1MuDTChambThContainer>(edmParameterSet.getParameter<edm::InputTag>("srcDTTh")),
           consumes<CSCCorrelatedLCTDigiCollection>(edmParameterSet.getParameter<edm::InputTag>("srcCSC")),
           consumes<RPCDigiCollection>(edmParameterSet.getParameter<edm::InputTag>("srcRPC"))}),
      m_Reconstruction(edmParameterSet, muStubsInputTokens) {
  produces<l1t::RegionalMuonCandBxCollection>("OMTF");

  /*inputTokenSimHit =
      consumes<edm::SimTrackContainer>(edmParameterSet.getParameter<edm::InputTag>("g4SimTrackSrc"));  //TODO remove*/

  if(edmParameterSet.exists("simTracksTag"))
    mayConsume<edm::SimTrackContainer>(edmParameterSet.getParameter<edm::InputTag>("simTracksTag") );
  if(edmParameterSet.exists("simVertexesTag"))
    mayConsume<edm::SimVertexContainer>(edmParameterSet.getParameter<edm::InputTag>("simVertexesTag") );
  if(edmParameterSet.exists("trackingParticleTag"))
    mayConsume<TrackingParticleCollection>(edmParameterSet.getParameter<edm::InputTag>("trackingParticleTag") );

  if(edmParameterSet.exists("rpcSimHitsInputTag"))
    mayConsume<edm::PSimHitContainer >(edmParameterSet.getParameter<edm::InputTag>("rpcSimHitsInputTag") );
  if(edmParameterSet.exists("cscSimHitsInputTag"))
    mayConsume<edm::PSimHitContainer >(edmParameterSet.getParameter<edm::InputTag>("cscSimHitsInputTag") );
  if(edmParameterSet.exists("dtSimHitsInputTag"))
    mayConsume<edm::PSimHitContainer >(edmParameterSet.getParameter<edm::InputTag>("dtSimHitsInputTag") );
}
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
L1TMuonOverlapPhase1TrackProducer::~L1TMuonOverlapPhase1TrackProducer() {}
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
void L1TMuonOverlapPhase1TrackProducer::beginJob() { m_Reconstruction.beginJob(); }
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
void L1TMuonOverlapPhase1TrackProducer::endJob() { m_Reconstruction.endJob(); }
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
void L1TMuonOverlapPhase1TrackProducer::beginRun(edm::Run const& run, edm::EventSetup const& iSetup) {
  m_Reconstruction.beginRun(run, iSetup);
}
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
void L1TMuonOverlapPhase1TrackProducer::produce(edm::Event& iEvent, const edm::EventSetup& evSetup) {
  std::ostringstream str;

  std::unique_ptr<l1t::RegionalMuonCandBxCollection> candidates = m_Reconstruction.reconstruct(iEvent, evSetup);

  iEvent.put(std::move(candidates), "OMTF");
}
/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(L1TMuonOverlapPhase1TrackProducer);
