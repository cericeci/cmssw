#ifndef MCTruth_MuonAssociator_recoMuonEDProducer_h
#define MCTruth_MuonAssociator_recoMuonEDProducer_h

#include "DataFormats/MuonReco/interface/Muon.h" 
#include "DataFormats/RecoCandidate/interface/TrackAssociation.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "SimMuon/MCTruth/interface/MuonAssociatorByHits.h"
#include <memory>

class MuonAssociator_recoMuonEDProducer : public edm::stream::EDProducer<> {
public:
  explicit MuonAssociator_recoMuonEDProducer(const edm::ParameterSet &);
  ~MuonAssociator_recoMuonEDProducer() override;

private:
  virtual void beginJob();
  void produce(edm::Event &, const edm::EventSetup &) override;
  virtual void endJob();

  edm::InputTag tracksTag;
  edm::InputTag tpTag;
  edm::EDGetTokenT<TrackingParticleCollection> tpToken_;
  edm::EDGetTokenT<edm::View<reco::Muon>> tracksToken_;
  bool getTracksFromRecoMuon;
  bool ignoreMissingTrackCollection;
  edm::ParameterSet parset_;
  MuonAssociatorByHits *associatorByHits;
};

#endif
