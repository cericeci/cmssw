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
                                               # 'omtfEventPrint'
                    ),
        categories=cms.untracked.vstring('l1tMuBayesEventPrint', 'OMTFReconstruction'), #, 'FwkReport'
        cout=cms.untracked.PSet(
                         threshold=cms.untracked.string('INFO'),
                         default=cms.untracked.PSet(limit=cms.untracked.int32(0)),
                         # INFO   =  cms.untracked.int32(0),
                         # DEBUG   = cms.untracked.int32(0),
                         l1tMuBayesEventPrint=cms.untracked.PSet(limit=cms.untracked.int32(1000000000)),
                         OMTFReconstruction=cms.untracked.PSet(limit=cms.untracked.int32(1000000000)),
                         #FwkReport=cms.untracked.PSet(reportEvery = cms.untracked.int32(50) ),
                       ), 
       debugModules=cms.untracked.vstring('simBayesOmtfDigis') 
       # debugModules = cms.untracked.vstring('*')
    )

#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(50)
process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(False),
                                         # SkipEvent = cms.untracked.vstring('ProductNotFound') 
                                     )

process.source = cms.Source('PoolSource',
 #fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/PhaseIITDRSpring19DR_Mu_FlatPt2to100_noPU_v31_E0D5C6A5-B855-D14F-9124-0B2C9B28D0EA_dump4000Ev.root")                     
 fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/PhaseIITDRSpring19DR_Mu_FlatPt2to100_noPU_v31_E0D5C6A5-B855-D14F-9124-0B2C9B28D0EA_dump4000Ev.root")
 #fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/DisplacedMuonGun_Pt30To100_Dxy_0_1000_34016F34-7F62-E911-AAB8-0025905AA9CC_dumpAllEv.root")
 )
	                    
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))

# PostLS1 geometry used
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
############################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')


####Event Setup Producer
process.load('L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff')
process.esProd = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(
      cms.PSet(record = cms.string('L1TMuonOverlapParamsRcd'),
               data = cms.vstring('L1TMuonOverlapParams'))
                   ),
   verbose = cms.untracked.bool(False)
)

process.TFileService = cms.Service("TFileService", fileName = cms.string('omtfAnalysis1.root'), closeFileFast = cms.untracked.bool(True) )
								
####OMTF Emulator
process.load('L1Trigger.L1TMuonOverlapPhase1.simBayesOmtfDigis_cfi')

process.simBayesOmtfDigis.dumpResultToXML = cms.bool(True)
process.simBayesOmtfDigis.rpcMaxClusterSize = cms.int32(3)
process.simBayesOmtfDigis.rpcMaxClusterCnt = cms.int32(2)
process.simBayesOmtfDigis.rpcDropAllClustersIfMoreThanMax = cms.bool(False)
process.simBayesOmtfDigis.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0005_1.xml")

process.simBayesOmtfDigis.lctCentralBx = cms.int32(8);#<<<<<<<<<<<<<<<<!!!!!!!!!!!!!!!!!!!!TODO this was changed in CMSSW 10(?) to 8. if the data were generated with the previous CMSSW then you have to use 6

#process.simBayesOmtfDigis.goldenPatternResultFinalizeFunction = cms.int32(6) #valid values are 0, 1, 2, 3, 5, 6, but for other then 0 the candidates quality assignemnt must be updated

process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")

process.L1TMuonSeq = cms.Sequence( process.esProd          
                                   + process.simBayesOmtfDigis 
                                   #+ process.dumpED
                                   #+ process.dumpES
)

process.L1TMuonPath = cms.Path(process.L1TMuonSeq)

process.out = cms.OutputModule("PoolOutputModule", 
   fileName = cms.untracked.string("l1tomtf_superprimitives1.root"),
   outputCommands = cms.untracked.vstring("drop *",
       "keep recoGenParticles_*_*_*",
       "keep *_genParticles_*_*",
       "keep l1tRegionalMuonCandBXVector_*_OMTF_*",)
)

process.output_step = cms.EndPath(process.out)
process.schedule = cms.Schedule(process.L1TMuonPath)
process.schedule.extend([process.output_step])
