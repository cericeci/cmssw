#include <L1Trigger/L1TMuonBayes/interface/Omtf/GhostBusterDropRB1.h>
#include <L1Trigger/L1TMuonBayes/interface/Omtf/OMTFConfiguration.h>
#include <sstream>

#include "FWCore/MessageLogger/interface/MessageLogger.h"

namespace { 

  int phiGMT(int phiAlgo) { return phiAlgo*437/pow(2,12); }

  struct AlgoMuonEtaFix : public AlgoMuon {
    AlgoMuonEtaFix(const AlgoMuon & mu) : AlgoMuon(mu), fixedEta(mu.getEta()) {}
    unsigned int fixedEta;
  };

}

AlgoMuons GhostBusterDropRB1::select(AlgoMuons muonsIN, int charge) {
  // sorting within GB.
  auto customLess = [&](const AlgoMuons::value_type& a, const AlgoMuons::value_type& b)->bool {
    int aRefLayerLogicNum = omtfConfig->getRefToLogicNumber()[a->getRefLayer()];
    int bRefLayerLogicNum = omtfConfig->getRefToLogicNumber()[b->getRefLayer()];
    if(a->getQ() > b->getQ())
      return false;
    else if(a->getQ()==b->getQ() && aRefLayerLogicNum < bRefLayerLogicNum) {
      return false;
    }
    else if (a->getQ()==b->getQ() && aRefLayerLogicNum == bRefLayerLogicNum && a->getDisc() > b->getDisc() )
      return false;
    else if (a->getQ()==b->getQ() && aRefLayerLogicNum == bRefLayerLogicNum && a->getDisc() == b->getDisc() && a->getPatternNumber() > b->getPatternNumber() )
      return false;
    else if (a->getQ()==b->getQ() && aRefLayerLogicNum == bRefLayerLogicNum && a->getDisc() == b->getDisc() && a->getPatternNumber() == b->getPatternNumber() && a->getRefHitNumber() < b->getRefHitNumber())
      return false;
    else
      return true;
  };

  std::sort( muonsIN.rbegin(), muonsIN.rend(), customLess);
  std::cout << "Sorting layers by " << std::endl;
  bool hasMB1  = false;
  bool hasRPB1 = false;
  for (const auto & muIN : muonsIN) {
      std::cout << omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()] << " , "; 
      if (omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==0 || omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==1) hasMB1 = true;
      if (omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==10 || omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==11) hasRPB1 = true;
  }
  std::cout << std::endl;

  for (const auto & muIN : muonsIN) {
      std::cout << muIN->getDisc() << " , "; 
  }

  std::cout << std::endl;
  // actual GhostBusting. Overwrite eta in case of no DT info.
  std::vector<AlgoMuonEtaFix> refHitCleanCandsFixedEta;
  for (const auto & muIN : muonsIN) {
    //It has to be done here, if we put it into the sorting "<" definition it stops being an strict order relation and std::sort is not reliable
    if (hasMB1 && ( omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==10 || omtfConfig->getRefToLogicNumber()[muIN->getRefLayer()]==11)) continue;
    refHitCleanCandsFixedEta.push_back( *muIN); //FIXME to much copying here...
    auto killIt = refHitCleanCandsFixedEta.end();
    //do not accept candidates with similar phi (any charge combination)
    //veto window 5 degree in GMT scale is 5/360*576=8 units
    for (auto it1 = refHitCleanCandsFixedEta.begin(); it1 != refHitCleanCandsFixedEta.end(); ++it1) {
      for (auto it2 = std::next(it1); it2 != refHitCleanCandsFixedEta.end(); ++it2) {
        if (it2->isValid() && std::abs( phiGMT(it1->getPhi()) - phiGMT(it2->getPhi()) ) < 8 ) {
          //Then, as we are underestimating the pdf for the MB1 (not adding RPB1 term), take it over the rest
          killIt = it2;
          if (hasMB1 && hasRPB1 && (omtfConfig->getRefToLogicNumber()[it2->getRefLayer()]==0 || omtfConfig->getRefToLogicNumber()[it2->getRefLayer()]==1)) killIt = it1;
          if (    (omtfConfig->fwVersion() >= 6)
               && ((abs(it1->getEta())==75 || abs(it1->getEta())==79 || abs(it1->getEta())==92))
               && ((abs(it2->getEta())!=75 && abs(it2->getEta())!=79 && abs(it2->getEta())!=92)) ) it1->fixedEta=it2->getEta();
        }
      }
    } 
    if (killIt != refHitCleanCandsFixedEta.end())
      refHitCleanCandsFixedEta.erase(killIt);
  }

  // fill outgoing collection 
  AlgoMuons refHitCleanCands;
  for (const auto & mu : refHitCleanCandsFixedEta) {
    AlgoMuon fixed = mu;
    fixed.setEta(mu.fixedEta);
    refHitCleanCands.emplace_back(new AlgoMuon(fixed) );
  } 

  while(refHitCleanCands.size() < 3)
    refHitCleanCands.emplace_back(new AlgoMuon());

  std::cout << "Selected layers by " << std::endl;
  for (const auto & mu : refHitCleanCands) {
      std::cout << omtfConfig->getRefToLogicNumber()[mu->getRefLayer()] << " , "; 
  }
  std::cout << std::endl; 
  for (const auto & mu : refHitCleanCands) {
      std::cout << mu->getDisc() << " , "; 
  }
  std::cout << std::endl; 
/*
  std::stringstream myStr;
  bool hasCandidates = false;
  for(unsigned int iRefHit=0;iRefHit<refHitCleanCands.size();++iRefHit){
    if(refHitCleanCands[iRefHit].getQ()){
      hasCandidates=true;
      break;
    }
  }
  for(unsigned int iRefHit=0;iRefHit<refHitCleanCands.size();++iRefHit){
    if(refHitCleanCands[iRefHit].getQ()) myStr<<"Ref hit: "<<iRefHit<<" "<<refHitCleanCands[iRefHit]<<std::endl;
  }
  if(hasCandidates) edm::LogInfo("OMTF Sorter")<<myStr.str();
*/

  return refHitCleanCands;
}
