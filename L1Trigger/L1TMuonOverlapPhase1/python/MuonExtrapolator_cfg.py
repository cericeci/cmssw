import FWCore.ParameterSet.Config as cms
dispGenEta  = cms.EDProducer("MuonExtrapolator",
                             src=cms.InputTag("genParticles","","HLT"),
                            )
