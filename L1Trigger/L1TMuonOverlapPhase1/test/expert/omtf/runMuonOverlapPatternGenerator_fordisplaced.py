# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms
process = cms.Process("L1TMuonEmulation")
import os
import sys
import commands
import re
from os import listdir
from os.path import isfile, join

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D41_cff')
#process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2023_realistic_v2', '') 

path = '/pool/phedex/userstorage/carlosec/omtf/privateSamples/' # Private displaced samples

firstEv = 0

process.source = cms.Source('PoolSource',
fileNames = cms.untracked.vstring( #'file:/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/test.root',#files,
    'file:/pool/phedex/userstorage/carlosec/omtf/privateSamples/custom_3.root' #UltraSkim of the private sample, training subset
    ),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    inputCommands=cms.untracked.vstring( #This speeds up read/write slightly
        'keep *',
        'drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT',
        'drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT',
        'drop l1tEMTFHit2016s_simEmtfDigis__HLT',
        'drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT',
        'drop l1tEMTFTrack2016s_simEmtfDigis__HLT'
    )
)

	                    
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))


####Event Setup Producer
process.load('L1Trigger.L1TMuonOverlapPhase1.fakeOmtfParams_cff')
process.esProd = cms.EDAnalyzer("EventSetupRecordDataGetter",
   toGet = cms.VPSet(
      cms.PSet(record = cms.string('L1TMuonOverlapParamsRcd'),
               data = cms.vstring('L1TMuonOverlapParams'))
                   ),
   verbose = cms.untracked.bool(False)
)

#process.TFileService = cms.Service("TFileService", fileName = cms.string('omtfAnalysis1_1.root'), closeFileFast = cms.untracked.bool(True) )
                                   
####OMTF Emulator
process.load('L1Trigger.L1TMuonOverlapPhase1.simBayesOmtfDigis_cfi')

# No need to dump everything for training
process.simBayesOmtfDigis.dumpResultToXML = cms.bool(False)
process.simBayesOmtfDigis.dumpResultToROOT = cms.bool(False)
process.simBayesOmtfDigis.eventCaptureDebug = cms.bool(False)

process.simBayesOmtfDigis.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0005_1.xml")
process.simBayesOmtfDigis.patternType = cms.string("GoldenPatternWithStat")
process.simBayesOmtfDigis.generatePatterns = cms.bool(True)
process.simBayesOmtfDigis.optimisedPatsXmlFile = cms.string("PatternsDisplaced_0x0005_2_optimized.xml")

process.simBayesOmtfDigis.rpcMaxClusterSize = cms.int32(3)
process.simBayesOmtfDigis.rpcMaxClusterCnt = cms.int32(2)
process.simBayesOmtfDigis.rpcDropAllClustersIfMoreThanMax = cms.bool(True)

#Part of the fix for the fake timing TPs
process.simBayesOmtfDigis.bxMin = cms.int32(-1)
#process.simBayesOmtfDigis.bxMax = cms.int32(4)

process.simBayesOmtfDigis.goldenPatternResultFinalizeFunction = cms.int32(5) #Ranges from  0, 1, 2, 3, 5
process.simBayesOmtfDigis.lctCentralBx = cms.int32(8);                       #Always tricky, use 6 for older ones

# In case we want to do multicore
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)

#process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
#process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")

process.L1TMuonSeq = cms.Sequence( process.esProd          
                                   + process.simBayesOmtfDigis 
                                   #+ process.dumpED
                                   #+ process.dumpES
)

process.L1TMuonPath = cms.Path(process.L1TMuonSeq)

