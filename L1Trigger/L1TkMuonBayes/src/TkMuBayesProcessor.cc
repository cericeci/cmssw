/*
 * TkMuBayesProcessor.cpp
 *
 *  Created on: Jan 18, 2019
 *      Author: kbunkow
 */

#include "L1Trigger/L1TkMuonBayes/interface/TkMuBayesProcessor.h"
#include "L1Trigger/L1TkMuonBayes/interface/PdfModuleWithStats.h"
#include <functional>

TkMuBayesProcessor::TkMuBayesProcessor(TkMuBayesProcConfigPtr& config, std::string pdfModuleType) : config(config) {
  if (pdfModuleType == "PdfModuleWithStats")
    pdfModule = std::make_unique<PdfModuleWithStats>(config);
  else
    pdfModule = std::make_unique<PdfModule>(config);

  ghostBustFunc = std::bind(&TkMuBayesProcessor::ghostBust4, this, std::placeholders::_1, std::placeholders::_2);
  //ghostBustFunc = std::bind(&TkMuBayesProcessor::ghostBust3, this, std::placeholders::_1, std::placeholders::_2);
}

TkMuBayesProcessor::TkMuBayesProcessor(TkMuBayesProcConfigPtr& config, unique_ptr<IPdfModule> pdfModule)
    : config(config), pdfModule(std::move(pdfModule)) {
  ghostBustFunc = std::bind(&TkMuBayesProcessor::ghostBust4, this, std::placeholders::_1, std::placeholders::_2);
  //ghostBustFunc = std::bind(&TkMuBayesProcessor::ghostBust3, this, std::placeholders::_1, std::placeholders::_2);

  ///FIXME: read the list from configuration so this can be controlled at runtime.
  lowQualityHitPatterns = {
      //                                                                                        987654321098765432109876543210
      //                                                                                               432143R2R143211B4B3B2B1
      std::pair<int, boost::dynamic_bitset<> >(
          4, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000010000000000001)),  //MB1, RB1in
      std::pair<int, boost::dynamic_bitset<> >(
          4, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000100000000000001)),  //MB1, RB1out
      std::pair<int, boost::dynamic_bitset<> >(
          4, boost::dynamic_bitset<>(config->nLayers(), 0b000000000010000000001000000000)),  //ME1/2  or ME1/3, RE1

      std::pair<int, boost::dynamic_bitset<> >(
          12, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000000000000000011)),
      std::pair<int, boost::dynamic_bitset<> >(
          12, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000000000000001100)),
      std::pair<int, boost::dynamic_bitset<> >(
          12, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000000000000110000)),
      std::pair<int, boost::dynamic_bitset<> >(
          12, boost::dynamic_bitset<>(config->nLayers(), 0b000000000000000000000011000000)),
      // std::pair<int, boost::dynamic_bitset<> >(4,  boost::dynamic_bitset<>(config->nLayers(), 0b000000010000000001000000000000) )
  };
}

TkMuBayesProcessor::~TkMuBayesProcessor() {
  // TODO Auto-generated destructor stub
}

AlgoTTMuons TkMuBayesProcessor::processTracks(const MuonStubsInput& muonStubs, const TrackingTriggerTracks& ttTracks) {
  AlgoTTMuons algoTTMuons;

  for (auto& ttTrack : ttTracks) {
    //TODO add switch to use either processTrack or processTrackUsingRefStubs

    //cout<<"\n"<<__FUNCTION__<<":"<<__LINE__<<" "<<*ttTrack<<std::endl;
    auto algoTTMuon = processTrack(muonStubs, ttTrack);

    if (algoTTMuon->getFiredLayerCnt() >= config->nMinFiredLayers()) {
      algoTTMuon->setValid(true);
      algoTTMuons.emplace_back(algoTTMuon);

      /*      LogTrace("l1tOmtfEventPrint")<<">>>>>>>>>>>>>>>>>>>>> algoTTMuon found for the ttTrack: \n "
          //<<" ttTrack Pt "<<ttTrack->getPt()<<" charge "<<ttTrack->getCharge()
          //<<" eta "<<ttTrack->getEta()<<" phi "<<ttTrack->getPhi()<<" index  "<<ttTrack->getIndex()<<"\n"
          <<*algoTTMuon<<endl;*/
    }
  }

  auto ghostBustedTTmuons = ghostBust(algoTTMuons);

  if (muTimingModule) {
    for (auto& ghostBustedTTmuon : ghostBustedTTmuons) {
      muTimingModule->process(ghostBustedTTmuon.get());
    }
  }

  assignQuality(ghostBustedTTmuons);

  //only debug
  /*  for(auto& ghostBustedTTmuon : ghostBustedTTmuons) {
    LogTrace("l1tOmtfEventPrint")<<">>>>>>>>>>>>>>>>>>>>> ghostBustedTTmuon: \n "
        <<*ghostBustedTTmuon<<endl;
  }*/

  //only debug
  for (auto& algoTTMuon : algoTTMuons) {
    auto& ttTrack = algoTTMuon->getTTTrack();
    LogTrace("l1tOmtfEventPrint") << ">>>>>>>>>>>>>>>>>>>>> algoTTMuon found for the ttTrack: \n "
                                  << " ttTrack Pt " << ttTrack->getPt() << " charge " << ttTrack->getCharge() << " eta "
                                  << ttTrack->getEta() << " phi " << ttTrack->getPhi() << " index  "
                                  << ttTrack->getIndex() << *algoTTMuon << endl;
  }

  return ghostBustedTTmuons;
}

AlgoTTMuonPtr TkMuBayesProcessor::processTrack(const MuonStubsInput& muonStubs,
                                               const TrackingTriggerTrackPtr& ttTrack) {
  //Selecting stubs that fit coarsely to the ttTrack, e.g. the full chambers
  MuonStubsInput selectedMuonStubs = selectStubs(muonStubs, ttTrack);

  AlgoTTMuonPtr algoTTMuon = std::make_shared<AlgoTTMuon>(ttTrack, config);
  for (unsigned int iLayer = 0; iLayer < config->nLayers(); ++iLayer) {
    processStubs(selectedMuonStubs, iLayer, ttTrack, MuonStubPtr(), algoTTMuon);
    //the muonStubs has no stubs in the banding layer, the phiB is processed wheh the corresponding phi layer is processed
  }

  return algoTTMuon;
}

AlgoTTMuonPtr TkMuBayesProcessor::processTrackUsingRefStubs(const MuonStubsInput& muonStubs,
                                                            const TrackingTriggerTrackPtr& ttTrack) {
  AlgoTTMuonPtr bestAlgoTTMuon;

  MuonStubsInput selectedMuonStubs = selectStubs(muonStubs, ttTrack);

  MuonStubPtrs1D refStubs = selectRefStubs(selectedMuonStubs, ttTrack);

  for (unsigned int iRefStub = 0; iRefStub < refStubs.size(); ++iRefStub) {
    AlgoTTMuonPtr algoTTMuon = std::make_shared<AlgoTTMuon>(ttTrack, config, refStubs[iRefStub]);
    for (unsigned int iLayer = 0; iLayer < config->nLayers(); ++iLayer) {
      processStubs(selectedMuonStubs, iLayer, ttTrack, refStubs[iRefStub], algoTTMuon);
    }

    //TODO do something better?
    if (algoTTMuon->getFiredLayerCnt() >= config->nMinFiredLayers()) {
      algoTTMuon->setValid(true);
    }

    if (algoTTMuon->isValid()) {
      if (!bestAlgoTTMuon ||  //TODO maybe better just use the pdfSum - check and optimize
          (algoTTMuon->getFiredLayerCnt() > bestAlgoTTMuon->getFiredLayerCnt()) ||
          (algoTTMuon->getFiredLayerCnt() == bestAlgoTTMuon->getFiredLayerCnt() &&
           algoTTMuon->getPdfSum() > bestAlgoTTMuon->getPdfSum())) {
        bestAlgoTTMuon = algoTTMuon;
      }
    }
  }

  return bestAlgoTTMuon;
}

MuonStubsInput TkMuBayesProcessor::selectStubs(const MuonStubsInput& muonStubs,
                                               const TrackingTriggerTrackPtr& ttTrack) {
  MuonStubsInput selectedMuonStubs(config.get());

  //TODO this implementation is rather not possible in the hardware, a different approach would be needed
  for (unsigned int iLayer = 0; iLayer < muonStubs.getMuonStubs().size(); ++iLayer) {
    for (auto& stub : muonStubs.getMuonStubs()[iLayer]) {
      if (config->isPhiLayer(iLayer)) {  //phi stubs, TODO add a better way to distinguish eta and phi stubs
        //for phi stubs, we simply check that the eta extent of the chamber is more or less compatible with the eta of the ttTrack
        //TODO for the moment any phi extrapolation is ignored, implement it (it should be something simple at this stage, i.e. e.g. not including the pt
        int etaMargin = stub->etaSigmaHw + 10;  //adding some additional margin, TODO optimize margin and move to config
        if (abs(stub->etaHw - ttTrack->getEtaHw()) < etaMargin) {
          selectedMuonStubs.addStub(iLayer, stub);
        }
      } else {
        //TODO implement something for the eta stubs
      }
    }
  }

  return selectedMuonStubs;
}

MuonStubPtrs1D TkMuBayesProcessor::selectRefStubs(const MuonStubsInput& muonStubs,
                                                  const TrackingTriggerTrackPtr& ttTrack) {
  MuonStubPtrs1D refStubs;
  //TODO implement
  return refStubs;
}

void TkMuBayesProcessor::processStubs(const MuonStubsInput& muonStubs,
                                      unsigned int layer,
                                      const TrackingTriggerTrackPtr& ttTrack,
                                      const MuonStubPtr refStub,
                                      AlgoTTMuonPtr algoTTMuon) {
  pdfModule->processStubs(muonStubs, layer, ttTrack, refStub, algoTTMuon);
}

AlgoTTMuons TkMuBayesProcessor::ghostBust(AlgoTTMuons& algoTTMuons) {
  AlgoTTMuons selectedTTMuons;
  for (auto& ttMuon : algoTTMuons) {
    for (auto& selected : selectedTTMuons) {
      int ghostBustResult = ghostBustFunc(selected, ttMuon);
      if (ghostBustResult & 2) {  //selected kills ttMuon
        ttMuon->kill();
      }
      if (ghostBustResult & 1) {  //ttMuon kills selected
        selected->kill();
      }
    }

    selectedTTMuons.erase(
        std::remove_if(selectedTTMuons.begin(), selectedTTMuons.end(), [](AlgoTTMuonPtr& x) { return x->isKilled(); }),
        selectedTTMuons.end());

    if (!ttMuon->isKilled()) {
      selectedTTMuons.push_back(ttMuon);
    }
  }

  return selectedTTMuons;
}

/**should return:
 * 0 none is killed
 * 1 first is killed
 * 2 second is killed
 * 3 both are killed
 */
int TkMuBayesProcessor::ghostBust3(std::shared_ptr<AlgoTTMuon> first, std::shared_ptr<AlgoTTMuon> second) {
  //cout<<__FUNCTION__<<":"<<__LINE__<<endl;
  //good ghost bust function looks on the hits indexes in each candidate and check how many hits are common, kill one of them if more then e.g. 1
  int commonHits = 0;
  for (unsigned int iLayer = 0; iLayer < first->getStubResults().size(); ++iLayer) {
    if (
        //first->isLayerFired(iLayer) &&
        //second->isLayerFired(iLayer) &&
        first->getStubResult(iLayer).getValid() && second->getStubResult(iLayer).getValid() &&
        first->getStubResult(iLayer).getMuonStub() ==
            second->getStubResult(iLayer)
                .getMuonStub()) {  //TODO comparing here just the pointer to the muon stub, in hardware probably it should be an index of the stub
      commonHits++;
    }
  }

  if (commonHits >= 1) {  //probably to sharp...
    if (first->getPdfSum() > second->getPdfSum()) {
      return 2;
    } else if (first->getPdfSum() < second->getPdfSum()) {
      return 1;
    } else {  // first->getGpResult().getPdfSum()== second->getGpResult().getPdfSum()
      if (first->getTTTrack()->getPtHw() > second->getTTTrack()->getPtHw())
        return 2;
      else
        return 1;
    }
  }
  return 0;
}

/**should return:
 * 0 none is killed
 * 1 first is killed
 * 2 second is killed
 * 3 both are killed
 */
int TkMuBayesProcessor::ghostBust4(std::shared_ptr<AlgoTTMuon> first, std::shared_ptr<AlgoTTMuon> second) {
  //cout<<__FUNCTION__<<":"<<__LINE__<<endl;
  //good ghost bust function looks on the hits indexes in each candidate and check how many hits are common, kill one of them if more then e.g. 1
  int commonHits = 0;
  for (unsigned int iLayer = 0; iLayer < first->getStubResults().size(); ++iLayer) {
    if (first->getStubResult(iLayer).getValid() && second->getStubResult(iLayer).getValid() &&
        first->getStubResult(iLayer).getMuonStub() == second->getStubResult(iLayer).getMuonStub()) {
      //TODO comparing here just the pointer to the muon stub, in hardware probably it should be an index of the stub

      if (first->getStubResult(iLayer).getPdfVal() > second->getStubResult(iLayer).getPdfVal()) {
        second->invalidateStubResult(iLayer);
      } else {
        first->invalidateStubResult(iLayer);
      }
      commonHits++;
    }
  }

  int result = 0;
  if (commonHits >= 1) {  //only then any can be killed
    if (first->getFiredLayerCnt() < config->nMinFiredLayers()) {
      result += 1;
    }
    if (second->getFiredLayerCnt() < config->nMinFiredLayers()) {
      result += 2;
    }
  }
  return result;
}
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

AlgoTTMuons TkMuBayesProcessor::processTracks(const StandaloneCandWithStubsVec& candsWithStubs,
                                              const TrackingTriggerTracks& ttTracks) {
  AlgoTTMuons algoTTMuons;

  for (auto& ttTrack : ttTracks) {
    //TODO add switch to use either processTrack or processTrackUsingRefStubs
    auto algoTTMuon = processTrack(candsWithStubs, ttTrack);

    if (algoTTMuon->getFiredLayerCnt() >= config->nMinFiredLayers()) {
      algoTTMuons.emplace_back(algoTTMuon);

      /*      LogTrace("l1tOmtfEventPrint")<<">>>>>>>>>>>>>>>>>>>>> algoTTMuon found for the ttTrack: \n "
          <<" ttTrack Pt "<<ttTrack->getPt()<<" charge "<<ttTrack->getCharge()
          <<" eta "<<ttTrack->getEta()<<" phi "<<ttTrack->getPhi()<<" index  "<<ttTrack->getIndex()
          <<*algoTTMuon<<endl;*/
    }
  }

  auto ghostBustedTTmuons = ghostBust(algoTTMuons);

  for (auto& algoTTMuon : algoTTMuons) {
    auto& ttTrack = algoTTMuon->getTTTrack();
    LogTrace("l1tOmtfEventPrint") << ">>>>>>>>>>>>>>>>>>>>> algoTTMuon found for the ttTrack: \n "
                                  << " ttTrack Pt " << ttTrack->getPt() << " charge " << ttTrack->getCharge() << " eta "
                                  << ttTrack->getEta() << " phi " << ttTrack->getPhi() << " index  "
                                  << ttTrack->getIndex() << *algoTTMuon << endl;
  }

  //only debug
  /*  for(auto& ghostBustedTTmuon : ghostBustedTTmuons) {
    LogTrace("l1tOmtfEventPrint")<<">>>>>>>>>>>>>>>>>>>>> ghostBustedTTmuon: \n "
        <<*ghostBustedTTmuon<<endl;
  }*/

  return ghostBustedTTmuons;
}

AlgoTTMuonPtr TkMuBayesProcessor::processTrack(const StandaloneCandWithStubsVec& candsWithStubs,
                                               const TrackingTriggerTrackPtr& ttTrack) {
  AlgoTTMuonPtr algoTTMuon = std::make_shared<AlgoTTMuon>(ttTrack, config);

  StandaloneCandWithStubsVec selectedStandaloneCands = selectCandsWithStubs(candsWithStubs, ttTrack);

  for (auto& candWithStubs : selectedStandaloneCands) {
    processTrack(candWithStubs.stubs, ttTrack);
  }

  return algoTTMuon;
}

StandaloneCandWithStubsVec TkMuBayesProcessor::selectCandsWithStubs(const StandaloneCandWithStubsVec& candsWithStubs,
                                                                    const TrackingTriggerTrackPtr& ttTrack) {
  StandaloneCandWithStubsVec selectedStandaloneCands;

  for (auto& candWithStubs : candsWithStubs) {
    //TODO implement
  }

  return selectedStandaloneCands;
}

/*std::vector<l1t::RegionalMuonCand> TkMuBayesProcessor::getFinalCandidates(unsigned int iProcessor, l1t::tftype mtfType, AlgoTTMuons& algoTTMuons) {
  std::vector<l1t::RegionalMuonCand> candidates;

  for(auto& algoTTMuon: algoTTMuons) {
    l1t::RegionalMuonCand candidate;
    candidate.setHwPt(algoTTMuon->getTTTrack()->getPtHw());
    candidate.setHwEta(algoTTMuon->getTTTrack()->getEtaHw());
    candidate.setHwPhi(config->phiToGlobalHwPhi(algoTTMuon->getTTTrack()->getPhi())); //TODO use hw phi

    candidate.setHwQual(algoTTMuon->getQuality());

    candidate.setHwSign(algoTTMuon->getTTTrack()->getCharge() < 0 ? 1 : 0  );
    candidate.setHwSignValid(1);

    std::map<int, int> trackAddr;
    trackAddr[0] = algoTTMuon->getFiredLayerBits().to_ulong();
    trackAddr[1] = 1234;//algoTTMuon->getRefLayer();
    trackAddr[2] = algoTTMuon->getPdfSum();
    trackAddr[3] = algoTTMuon->getTTTrack()->getIndex();
    candidate.setTrackAddress(trackAddr);
    candidate.setTFIdentifiers(iProcessor,mtfType);

    if (candidate.hwPt() > 0)
      candidates.push_back(candidate);
  }
  return candidates;
}*/

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
l1t::TkMuonBayesTrackCollection TkMuBayesProcessor::getMuCorrTrackCollection(unsigned int iProcessor,
                                                                             AlgoTTMuons& algoTTMuons) {
  l1t::TkMuonBayesTrackCollection candidates;

  for (auto& algoTTMuon : algoTTMuons) {
    if (algoTTMuon->getTTTrack()->getTTTrackPtr().isNonnull()) {
      candidates.emplace_back(algoTTMuon->getTTTrack()->getTTTrackPtr());
      //todo id needed set also setTrackPartPtr and setSimTrackPtr - but non the TrackingTriggerTrack can contain only one these 3 pointers
      //    candidates.back().setSimTrackPtr(algoTTMuon->getTTTrack()->getSimTrackPtr());
      //    candidates.back().setTrackPartPtr(algoTTMuon->getTTTrack()->getTrackingParticlePtr());
    } else if (algoTTMuon->getTTTrack()->getTrackingParticlePtr().isNonnull()) {
      candidates.emplace_back(algoTTMuon->getTTTrack()->getTrackingParticlePtr()->p4());
      candidates.back().setTrackPartPtr(algoTTMuon->getTTTrack()->getTrackingParticlePtr());
    } else if (algoTTMuon->getTTTrack()->getSimTrackRef().isNonnull()) {
      candidates.emplace_back(algoTTMuon->getTTTrack()->getSimTrackRef()->momentum());
      candidates.back().setSimTrackPtr(algoTTMuon->getTTTrack()->getSimTrackRef());
    } else {
      throw cms::Exception(
          "TkMuBayesProcessor::getMuCorrTrackCollection(): no pointer to construct l1t::TkMuonBayesTrack");
    }

    l1t::TkMuonBayesTrack& candidate = candidates.back();
    candidate.setHwPt(algoTTMuon->getTTTrack()->getPtHw());
    candidate.setHwEta(algoTTMuon->getTTTrack()->getEtaHw());
    candidate.setHwPhi(config->phiToGlobalHwPhi(algoTTMuon->getTTTrack()->getPhi()));  //TODO use hw phi

    candidate.setHwQual(algoTTMuon->getQuality());

    candidate.setHwSign(algoTTMuon->getTTTrack()->getCharge() < 0 ? 1 : 0);
    //candidate.setHwSignValid(1);
    candidate.setCharge(algoTTMuon->getTTTrack()->getCharge());

    candidate.setFiredLayerBits(algoTTMuon->getFiredLayerBits());
    candidate.setPdfSum(algoTTMuon->getPdfSum());

    if (algoTTMuon->getFiredLayerCnt(0) >= config->nMinFiredLayers())
      candidate.setCandidateType(l1t::TkMuonBayesTrack::fastTrack);
    else
      candidate.setCandidateType(l1t::TkMuonBayesTrack::slowTrack);

    candidate.setBeta(algoTTMuon->getBeta());
    candidate.setBetaLikelihood(algoTTMuon->getBetaLikelihood());
  }
  return candidates;
}

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////

bool TkMuBayesProcessor::assignQuality(AlgoTTMuons& algoTTMuons) {
  for (auto& algoTTMuon : algoTTMuons) {
    for (auto& firedLayers : lowQualityHitPatterns) {
      algoTTMuon->setQuality(13);  //Default quality
      if (firedLayers.second == algoTTMuon->getFiredLayerBits()) {
        algoTTMuon->setQuality(firedLayers.first);
        //LogTrace("l1tOmtfEventPrint")<<"demoting quality for "<<*algoTTMuon<<endl;
        break;
      }
    }
  }

  return true;
}
