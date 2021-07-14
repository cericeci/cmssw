# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms
process = cms.Process("L1TMuonEmulation")
import os
import sys
import commands

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.MessageLogger = cms.Service("MessageLogger",
        # suppressInfo       = cms.untracked.vstring('AfterSource', 'PostModule'),
        destinations=cms.untracked.vstring(
                                               # 'detailedInfo',
                                               # 'critical',
                                               'cout',
                                               #'cerr',
                                                'omtfEventPrint'
                    ),
        categories=cms.untracked.vstring('l1tMuBayesEventPrint', 'OMTFReconstruction'), #, 'FwkReport'
        cout=cms.untracked.PSet(
                         threshold=cms.untracked.string('DEBUG'),
                         default=cms.untracked.PSet(limit=cms.untracked.int32(0)),
                         # INFO   =  cms.untracked.int32(0),
                         # DEBUG   = cms.untracked.int32(0),
                         l1tMuBayesEventPrint=cms.untracked.PSet(limit=cms.untracked.int32(1000000000)),
                         OMTFReconstruction=cms.untracked.PSet(limit=cms.untracked.int32(1000000000)),
                         #FwkReport=cms.untracked.PSet(reportEvery = cms.untracked.int32(50) ),
                       ),
       debugModules=cms.untracked.vstring('simOmtfPhase1Digis','simOmtfPhase1DigisBoth','simOmtfPhase1DigisDisplaced')
       # debugModules = cms.untracked.vstring('*')
    )

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False),
                                         # SkipEvent = cms.untracked.vstring('ProductNotFound')
                                     )

process.source = cms.Source('PoolSource',
fileNames = cms.untracked.vstring("file:///nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/Run3_Fixed.root",)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))

# PostLS1 geometry used
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
############################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')


####Event Setup Producer
process.load('L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff')
process.omtfParams.configXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/hwToLogicLayer_0x0007.xml") ### Need to check the latest one
process.esProd = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(
      cms.PSet(record = cms.string('L1TMuonOverlapParamsRcd'),
               data = cms.vstring('L1TMuonOverlapParams'))
                   ),
   verbose = cms.untracked.bool(False)
)

####OMTF Emulator
process.load('L1Trigger.L1TMuonOverlapPhase1.simOmtfPhase1Digis_cfi')
process.simOmtfPhase1Digis.dumpResultToXML = cms.bool(True)
process.simOmtfPhase1Digis.rpcMaxClusterSize = cms.int32(3)
process.simOmtfPhase1Digis.rpcMaxClusterCnt = cms.int32(2)
process.simOmtfPhase1Digis.rpcDropAllClustersIfMoreThanMax = cms.bool(True)
process.simOmtfPhase1Digis.lctCentralBx = cms.int32(8)  # <<<<<<<<<<<<<<<<Warning! this was changed in CMSSW 10(?) to 8. if the data were generated with the previous CMSSW then you have to use 6

# Now clone it to run the displaced only omtf, need to check the latest patterns for the prompt
process.simOmtfPhase1Digis.patternsXMLFiles  = cms.VPSet( cms.PSet( patternsXMLFile =  cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x0003.xml")))
process.simOmtfPhase1DigisDisplaced = process.simOmtfPhase1Digis.clone()
process.simOmtfPhase1DigisDisplaced.patternsXMLFiles = cms.VPSet(cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0011_plus.xml")), cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0011_minus.xml")))
process.simOmtfPhase1DigisBoth = process.simOmtfPhase1Digis.clone()
process.simOmtfPhase1DigisBoth.patternsXMLFiles = cms.VPSet( cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0011_plus.xml")), cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0011_minus.xml")), cms.PSet( patternsXMLFile =  cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x0003.xml")))

process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")


#### Muon extrapolation for those that are generated as displaced -this should only run on MC-
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")
process.load("L1Trigger.L1TMuonOverlapPhase1.MuonExtrapolator_cfg")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.dispSeq = cms.Sequence(process.dispGenEta)
process.dispPath = cms.Path(process.dispSeq)

#Parallel running
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

process.L1TMuonSeq = cms.Sequence( process.esProd
                                   + process.simOmtfPhase1Digis
                                   + process.simOmtfPhase1DigisDisplaced
                                   + process.simOmtfPhase1DigisBoth
                                   + process.dispGenEta
)

process.L1TMuonPath = cms.Path(process.L1TMuonSeq)

### Some output cleanup
process.out = cms.OutputModule("PoolOutputModule",
   fileName = cms.untracked.string("l1tomtf_superprimitives1_allstrategies.root"),
   outputCommands = cms.untracked.vstring("drop *",
       "keep recoGenParticles_*_*_*",
       "keep *_genParticles_*_*",
       "keep l1tRegionalMuonCandBXVector_*_OMTF_*",
       "keep dispGenEta_*_*_*")
)

process.output_step = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.L1TMuonPath)
process.schedule.extend([process.output_step])
