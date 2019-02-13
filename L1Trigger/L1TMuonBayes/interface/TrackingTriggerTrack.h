/*
 * TrackingTriggerTrack.h
 *
 *  Created on: Jan 25, 2019
 *      Author: Karol Bunkowski kbunkow@cern.ch
 */

#ifndef L1TMUONBAYES_TRACKINGTRIGGERTRACK_H_
#define L1TMUONBAYES_TRACKINGTRIGGERTRACK_H_
#include "SimDataFormats/Track/interface/SimTrack.h"

#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"
#include "DataFormats/L1TrackTrigger/interface/TTTypes.h"

class TrackingTriggerTrack {
public:
/*  TrackingTriggerTrack(double phi, double eta,  double pt, int charge) : phi(phi), eta(eta), pt(pt), charge(charge) {
    //todo convert to hw scale
  };

  TrackingTriggerTrack(int phiHw, int etaHw,  int ptHw, int charge) : charge(charge), phiHw(phiHw), etaHw(etaHw), ptHw(ptHw) {
    //todo convert to physics scale
  };*/

  TrackingTriggerTrack(const SimTrack& simMuon);

  TrackingTriggerTrack(const TTTrack< Ref_Phase2TrackerDigi_>& ttTRack, unsigned int index, int l1Tk_nPar);

  int getCharge() const {
    return charge;
  }

  double getEta() const {
    return eta;
  }

  double getPhi() const {
    return phi;
  }

  double getPt() const {
    return pt;
  }

  int getEtaHw() const {
    return etaHw;
  }

  int getPhiHw() const {
    return phiHw;
  }

  int getPtHw() const {
    return ptHw;
  }

  void setEtaHw(int etaHw = 0) {
    this->etaHw = etaHw;
  }

  void setPhiHw(int phiHw = 0) {
    this->phiHw = phiHw;
  }

  void setPtHw(int ptHw = 0) {
    this->ptHw = ptHw;
  }

  //index in the tTTrackHandle
  unsigned int getIndex() const {
    return index;
  }

  unsigned int getEtaBin() const {
    return etaBin;
  }

  void setEtaBin(unsigned int etaBin = 0) {
    this->etaBin = etaBin;
  }

  unsigned int getPtBin() const {
    return ptBin;
  }

  void setPtBin(unsigned int ptBin = 0) {
    this->ptBin = ptBin;
  }


  friend std::ostream & operator << (std::ostream &out, const TrackingTriggerTrack& ttTrack);
private:
  double phi = 0;
  double eta = 0;
  double pt = 0;
  int charge = 0;


  ///in integer hardware scales
  int phiHw = 0;
  int etaHw = 0;
  int ptHw = 0;


  //used to address the LUTs
  unsigned int ptBin = 0;
  unsigned int etaBin = 0;

  unsigned int index = 0;
};

typedef std::shared_ptr<const TrackingTriggerTrack> TrackingTriggerTrackPtr;
typedef std::vector<TrackingTriggerTrackPtr> TrackingTriggerTracks;


#endif /* INTERFACE_TRACKINGTRIGGERTRACK_H_ */
