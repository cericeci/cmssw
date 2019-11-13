#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/RecoCandidate/interface/TrackAssociation.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "SimMuon/MCTruth/plugins/MuonAssociator_recoMuonEDProducer.h"
#include <memory>

MuonAssociator_recoMuonEDProducer::MuonAssociator_recoMuonEDProducer(const edm::ParameterSet &parset)
    : tracksTag(parset.getParameter<edm::InputTag>("tracksTag")),
      tpTag(parset.getParameter<edm::InputTag>("tpTag")),
      ignoreMissingTrackCollection(parset.getUntrackedParameter<bool>("ignoreMissingTrackCollection", false)),
      parset_(parset) {
  edm::LogVerbatim("MuonAssociator_recoMuonEDProducer") << "constructing  MuonAssociator_recoMuonEDProducer";
  produces<reco::RecoMuToSimCollection>();
  produces<reco::SimToRecoMuCollection>();
  tpToken_ = consumes<TrackingParticleCollection>(tpTag);
  tracksToken_ = consumes<edm::View<reco::Muon>>(tracksTag);

  /// Perform some sanity checks of the configuration
  LogTrace("MuonAssociator_recoMuonEDProducer") << "constructing  MuonAssociatorByHits" << parset_.dump();
  edm::LogVerbatim("MuonAssociator_recoMuonEDProducer") << "\n MuonAssociatorByHits will associate reco::Tracks with "
                                               << tracksTag << "\n\t\t and TrackingParticles with " << tpTag;
  const std::string recoTracksLabel = tracksTag.label();
  const std::string recoTracksInstance = tracksTag.instance();

  // check and fix inconsistent input settings
  // tracks with hits only on muon detectors
  if (recoTracksLabel == "standAloneMuons" || recoTracksLabel == "standAloneSETMuons" ||
      recoTracksLabel == "cosmicMuons" || recoTracksLabel == "hltL2Muons") {
    if (parset_.getParameter<bool>("UseTracker")) {
      edm::LogWarning("MuonAssociator_recoMuonEDProducer")
          << "\n*** WARNING : inconsistent input tracksTag = " << tracksTag << "\n with UseTracker = true"
          << "\n ---> setting UseTracker = false ";
      parset_.addParameter<bool>("UseTracker", false);
    }
    if (!parset_.getParameter<bool>("UseMuon")) {
      edm::LogWarning("MuonAssociator_recoMuonEDProducer")
          << "\n*** WARNING : inconsistent input tracksTag = " << tracksTag << "\n with UseMuon = false"
          << "\n ---> setting UseMuon = true ";
      parset_.addParameter<bool>("UseMuon", true);
    }
  }
  // tracks with hits only on tracker
  if (recoTracksLabel == "generalTracks" || recoTracksLabel == "ctfWithMaterialTracksP5LHCNavigation" ||
      recoTracksLabel == "hltL3TkTracksFromL2" ||
      (recoTracksLabel == "hltL3Muons" && recoTracksInstance == "L2Seeded")) {
    if (parset_.getParameter<bool>("UseMuon")) {
      edm::LogWarning("MuonAssociator_recoMuonEDProducer")
          << "\n*** WARNING : inconsistent input tracksTag = " << tracksTag << "\n with UseMuon = true"
          << "\n ---> setting UseMuon = false ";
      parset_.addParameter<bool>("UseMuon", false);
    }
    if (!parset_.getParameter<bool>("UseTracker")) {
      edm::LogWarning("MuonAssociator_recoMuonEDProducer")
          << "\n*** WARNING : inconsistent input tracksTag = " << tracksTag << "\n with UseTracker = false"
          << "\n ---> setting UseTracker = true ";
      parset_.addParameter<bool>("UseTracker", true);
    }
  }
  getTracksFromRecoMuon = true;
  if (recoTracksLabel == "hltL3Muons" || recoTracksLabel == "hltL3NoIDMuons"){
    getTracksFromRecoMuon = true;
  }

  LogTrace("MuonAssociator_recoMuonEDProducer") << "MuonAssociator_recoMuonEDProducer::beginJob "
                                          ": constructing MuonAssociatorByHits";
  associatorByHits = new MuonAssociatorByHits(parset_, consumesCollector());
}

MuonAssociator_recoMuonEDProducer::~MuonAssociator_recoMuonEDProducer() {}

void MuonAssociator_recoMuonEDProducer::beginJob() {}

void MuonAssociator_recoMuonEDProducer::endJob() {}

void MuonAssociator_recoMuonEDProducer::produce(edm::Event &event, const edm::EventSetup &setup) {
  using namespace edm;

  Handle<TrackingParticleCollection> TPCollection;
  LogTrace("MuonAssociator_recoMuonEDProducer") << "getting TrackingParticle collection - " << tpTag;
  event.getByToken(tpToken_, TPCollection);
  LogTrace("MuonAssociator_recoMuonEDProducer") << "\t... size = " << TPCollection->size();

  Handle<edm::View<reco::Track>> trackCollection;
  Handle<edm::View<reco::Muon>>  muonCollection;
  std::cout << "getting reco::Track collection - " << tracksTag << std::endl;
  bool trackAvailable;
  if (not getTracksFromRecoMuon){
    trackAvailable = event.getByToken(tracksToken_, trackCollection);
  }
  else {
    trackAvailable = event.getByToken(tracksToken_, muonCollection);
  }

  if (trackAvailable)
    std::cout << "\t... size = " << muonCollection->size() << std::endl;
  else
    std::cout << "\t... NOT FOUND." << std::endl;

  std::unique_ptr<reco::RecoMuToSimCollection> rts;
  std::unique_ptr<reco::SimToRecoMuCollection> str;

  if (ignoreMissingTrackCollection && !trackAvailable) {
    // the track collection is not in the event and we're being told to ignore
    // this. do not output anything to the event, other wise this would be
    // considered as inefficiency.
    std::cout << "\n ignoring missing track collection."
                                         << "\n";
  } else {
    std::cout
        << "\n >>> RecoToSim association <<< \n"
        << "     Track collection : " << tracksTag.label() << ":" << tracksTag.instance()
        << " (size = " << muonCollection->size() << ") \n"
        << "     TrackingParticle collection : " << tpTag.label() << ":" << tpTag.instance()
        << " (size = " << TPCollection->size() << ")" << std::endl; 

    reco::RecoMuToSimCollection recSimColl =
        associatorByHits->associateRecoToSim(muonCollection, TPCollection, &event, &setup);

    edm::LogVerbatim("MuonAssociator_recoMuonEDProducer")
        << "\n >>> SimToReco association <<< \n"
        << "     TrackingParticle collection : " << tpTag.label() << ":" << tpTag.instance()
        << " (size = " << TPCollection->size() << ") \n"
        << "     Track collection : " << tracksTag.label() << ":" << tracksTag.instance()
        << " (size = " << muonCollection->size() << ")";

    reco::SimToRecoMuCollection simRecColl =
        associatorByHits->associateSimToReco(muonCollection, TPCollection, &event, &setup);

    rts.reset(new reco::RecoMuToSimCollection(recSimColl));
    str.reset(new reco::SimToRecoMuCollection(simRecColl));

    event.put(std::move(rts));
    event.put(std::move(str));
  }
}
