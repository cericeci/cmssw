/*
 * AlgoTTMuon.h
 *
 *  Created on: Feb 1, 2019
 *      Author: Karol Bunkowski kbunkow@cern.ch
 */

#ifndef MUCORRELATOR_ALGOTTMUON_H_
#define MUCORRELATOR_ALGOTTMUON_H_

#include <vector>
#include <memory>
#include "boost/dynamic_bitset.hpp"

#include "L1Trigger/L1TMuonBayes/interface/TrackingTriggerTrack.h"
#include "L1Trigger/L1TMuonBayes/interface/MuonStub.h"
#include "L1Trigger/L1TMuonBayes/interface/StubResult.h"

#include "L1Trigger/L1TMuonBayes/interface/MuCorrelator/MuCorrelatorConfig.h"

class AlgoTTMuon {
public:
  AlgoTTMuon(const TrackingTriggerTrackPtr& ttTrack, MuCorrelatorConfigPtr& config):
    firedLayerBits(config->nLayers()), ttTrack(ttTrack), stubResults(config->nLayers()) {};

  AlgoTTMuon(const TrackingTriggerTrackPtr& ttTrack, MuCorrelatorConfigPtr& config, const MuonStubPtr& refStub):
    firedLayerBits(config->nLayers()), ttTrack(ttTrack), stubResults(config->nLayers()), refStub(refStub) {};

  virtual ~AlgoTTMuon() {};

  virtual void addStubResult(float pdfVal, bool valid, int pdfBin, int layer, MuonStubPtr stub);

  bool isValid() const {
    //TODO where and when it should be set?
    return valid;
  }

  void setValid(bool valid) {
    this->valid = valid;
  }

  unsigned int getFiredLayerCnt() const {
    return firedLayerBits.count();
  }

  double getPdfSum() const  {
    return pdfSum;
  }

  const bool isKilled() const {
    return killed;
  }

  void kill() {
    killed = true;
    //FIXME maybe also valid = false???
  }

  bool isLayerFired(unsigned int iLayer) const {
    return firedLayerBits[iLayer];
  }


  const TrackingTriggerTrackPtr& getTTTrack() const {
    return ttTrack;
  }
  const StubResult& getStubResult(unsigned int iLayer) const {
    return stubResults.at(iLayer);
  }

  const StubResults& getStubResults() const {
    return stubResults;
  }

  friend std::ostream & operator << (std::ostream &out, const AlgoTTMuon& algoTTMuon);

  const boost::dynamic_bitset<>& getFiredLayerBits() const {
    return firedLayerBits;
  }

private:
  bool valid = false;

  double pdfSum = 0;

  bool killed = false;

  ///Number of fired layers - excluding bending layers
  //unsigned int firedLayerCnt = 0;

  ///bits representing fired logicLayers (including bending layers),
  boost::dynamic_bitset<> firedLayerBits;

  //ttTrack, stubResults and refStub should be needed in the emulation (debugging etc), but not in the firmware

  TrackingTriggerTrackPtr ttTrack;

  StubResults stubResults;

  MuonStubPtr refStub;
};

typedef std::shared_ptr<AlgoTTMuon> AlgoTTMuonPtr;
typedef std::vector<AlgoTTMuonPtr> AlgoTTMuons;


#endif /* MUCORRELATOR_ALGOTTMUON_H_ */
