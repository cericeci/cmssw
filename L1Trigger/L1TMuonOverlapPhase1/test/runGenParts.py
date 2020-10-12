import FWCore.ParameterSet.Config as cms
process = cms.Process("MuonMatcher")

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))

process.source = cms.Source('PoolSource',
 fileNames = cms.untracked.vstring('file:///nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/l1tomtf_superprimitives1.root',
 )                           
)
	                    
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
# PostLS1 geometry used
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.MagneticField_cff')

############################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2023_realistic_v2', '')

process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")

####Event Setup Producer
process.load("L1Trigger.L1TMuonOverlapPhase1.MuonMatcher_cfg")

process.dispSeq = cms.Sequence( process.dispGenEta 
)

process.dispPath = cms.Path(process.dispSeq)

process.out = cms.OutputModule("PoolOutputModule", 
   fileName = cms.untracked.string("l1tomtf_superprimitives1_withgen_PROMPT.root")
)

process.output_step = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.dispPath)
process.schedule.extend([process.output_step])
