#ifndef DataRecords_L1TMuonEndCapForestO2ORcd_h
#define DataRecords_L1TMuonEndCapForestO2ORcd_h

#include "FWCore/Framework/interface/EventSetupRecordImplementation.h"
#include "CondFormats/DataRecord/interface/L1TriggerKeyListExtRcd.h"
#include "CondFormats/DataRecord/interface/L1TriggerKeyExtRcd.h"
#include "CondFormats/DataRecord/interface/L1TMuonEndCapForestRcd.h"

class L1TMuonEndCapForestO2ORcd
    : public edm::eventsetup::DependentRecordImplementation<
          L1TMuonEndCapForestO2ORcd,
          edm::mpl::Vector<L1TriggerKeyListExtRcd, L1TriggerKeyExtRcd, L1TMuonEndCapForestRcd> > {};

#endif
