import FWCore.ParameterSet.Config as cms

process = cms.Process("GEN")

process.options = cms.untracked.PSet(
  wantSummary = cms.untracked.bool( True )
)

process.source = cms.Source("EmptySource")

process.testRadix = cms.EDProducer('testRadix',
)

process.path = cms.Path(process.testRadix)

process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("testRadix.root"),
  outputCommands = cms.untracked.vstring(
    'drop *')
)

process.endp = cms.EndPath(process.out)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32( 1 )
)
