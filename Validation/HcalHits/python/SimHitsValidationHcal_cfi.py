import FWCore.ParameterSet.Config as cms

simHitsValidationHcal = cms.EDAnalyzer("SimHitsValidationHcal",
    ModuleLabel   = cms.string('g4SimHits'),
    HitCollection = cms.string('HcalHits'),
    Verbose       = cms.bool(False),
    TestNumber    = cms.bool(False),
)

from Configuration.Eras.Modifier_fastSim_cff import fastSim
fastSim.toModify( simHitsValidationHcal, ModuleLabel = cms.string("famosSimHits") )
