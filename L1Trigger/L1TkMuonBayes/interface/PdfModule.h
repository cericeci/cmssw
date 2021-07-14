/*
 * PdfModule.h
 *
 *  Created on: Feb 4, 2019
 *      Author: Karol Bunkowski kbunkow@cern.ch
 */

#ifndef L1TkMuonBayes_PDFMODULE_H_
#define L1TkMuonBayes_PDFMODULE_H_

#include "L1Trigger/L1TkMuonBayes/interface/AlgoTTMuon.h"
#include "L1Trigger/L1TkMuonBayes/interface/TkMuBayesProcConfig.h"
#include "L1Trigger/L1TMuonOverlapPhase1/interface/MuonStubsInput.h"

#include <vector>
#include <boost/serialization/access.hpp>
#include <boost/serialization/vector.hpp>

class IPdfModule {
public:
  IPdfModule(TkMuBayesProcConfigPtr config) : config(config) {}

  virtual ~IPdfModule() {}

  //virtual int getExtrapolation();

  //virtual void processStub(const MuonStubPtr& stub, int layer, const TrackingTriggerTrackPtr& ttTrack, const MuonStubPtr refStub, AlgoTTMuonPtr algoTTMuon) = 0;

  virtual void processStubs(const MuonStubsInput& muonStubs,
                            unsigned int layer,
                            const TrackingTriggerTrackPtr& ttTrack,
                            const MuonStubPtr refStub,
                            AlgoTTMuonPtr algoTTMuon) = 0;

protected:
  TkMuBayesProcConfigPtr config;
};

class PdfModule : public IPdfModule {
public:
  PdfModule(TkMuBayesProcConfigPtr& config);

  ~PdfModule() override {}

  //assign the coefficients vectors and fills it with some dummy values
  virtual void init();

  //adds the StubResult to the algoTTMuon
  void processStubs(const MuonStubsInput& muonStubs,
                            unsigned int layer,
                            const TrackingTriggerTrackPtr& ttTrack,
                            const MuonStubPtr refStub,
                            AlgoTTMuonPtr algoTTMuon) override;

  virtual float getExtrapolation(unsigned int layer,
                                 unsigned int etaBin,
                                 unsigned int refLayer,
                                 const TrackingTriggerTrackPtr& ttTrack);

  //refLayer = 0 means no ref layer is used, pdfBin is deltaPhi or deltaEta
  virtual float getPdfVal(unsigned int layer,
                          unsigned int etaBin,
                          unsigned int refLayer,
                          const TrackingTriggerTrackPtr& ttTrack,
                          int pdfBin);

  const std::vector<std::vector<std::vector<std::vector<std::vector<int> > > > >& getCoefficients() const {
    return coefficients;
  }

  //delta phi or delta eta to the given layer
  //virtual int getExtrapolation(int layer, cogenerateCoefficients: 155 iLayer 0 iEtaBin 0 iRefLayer 0 ptBin 63 a       2799 b         10 c        902nst TrackingTriggerTrackPtr& ttTrack, const MuonStubPtr refStub);

  //typedef boost::multi_array<PdfValueType, 3> pdfArrayType;
  //typedef boost::multi_array<short, 3> meanDistPhiArrayType;

  friend class boost::serialization::access;

  template <class Archive>
  void serialize(Archive& ar, const unsigned int version) {
    ar& BOOST_SERIALIZATION_NVP(bitShift);
    ar& BOOST_SERIALIZATION_NVP(coefficients);
  }

protected:
  //[layer][etaBin][refLayerNum][ptBin][coefficient index] refLayer = 0 means no ref layer, i.e. pdfBin = phiHit - phiTTTrack, otherwise pdfBin = phiHit - phiTTTrack - phiRefHit
  //pdfVal = a2(pdfBin -a1)^2 - a0
  std::vector<std::vector<std::vector<std::vector<std::vector<int> > > > > coefficients;

  int bitShift = 9;

  //boost::multi_array<short, 3> coefficients; -  cannot be use since the lengths of vectors varies between layers (1 eta bin for barrel layer, 8 or 16 for endcap)
};

#endif /* L1TkMuonBayes_PDFMODULE_H_ */
