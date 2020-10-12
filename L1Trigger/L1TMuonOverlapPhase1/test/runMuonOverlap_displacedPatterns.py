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
fileNames = cms.untracked.vstring(
"file:///nfs/fanae/user/carlosec/OMTF_2020/samples/custom_3.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/025D27E1-8363-B54D-8E59-15E4E4D8D0A4.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/23509529-CA46-0D44-91B3-CA5B0CD03AB5.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/3D6E0381-37F8-CA44-99D2-F0F07A27AB2A.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/41A8FF37-7D2E-7249-B152-FE89164826F2.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/4B69420D-7BBC-BC46-8FF8-4090BB22E52F.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/560F7499-5721-654B-BC83-3AE76477D8F1.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/6EA092BE-94A5-AD49-80DB-6A73ADBD033E.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/77DD67E9-434B-8242-B08C-C99FBC95F477.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/7E51FB46-8F9C-614D-830E-1DC00A69B753.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/7EABBE9A-4C49-BA4C-87C9-8E7E245174B3.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/7F4AF09D-D268-C74E-B06C-259D965857BE.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/871278EB-3E2F-4342-B4CF-B7BDBF38975A.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/918902A9-9C86-A04C-B4F1-EADCD16A7E22.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/97A0EE28-28BF-7249-9A3F-772D6B7A98A3.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/A87AA119-9C11-3A49-B726-D87465854A19.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/AA5992F4-5D03-BF41-8CA6-0C0F5B38EC1E.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/B43C1523-B66F-944D-A2E9-128CB4576CF8.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/BBDD1FC4-DC6F-1F4C-B777-72D247A6FC1F.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/BDCB64F7-4BC6-D342-B4E7-F9451C5656D0.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/D696E7CC-7F02-CA4C-83C9-DD51FBCD3A48.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/DBDE8ECA-27FA-3D49-AE4A-8ACC528A853A.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/DD924933-8A75-8645-84F5-D408236797C1.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/DEE59424-11F1-B34E-A151-77D6642AA834.root",
#"file:///pool/phedex/userstorage/carlosec/omtf/inputs/prompt/E0D5C6A5-B855-D14F-9124-0B2C9B28D0EA.root",
#fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/PhaseIITDRSpring19DR_Mu_FlatPt2to100_noPU_v31_E0D5C6A5-B855-D14F-9124-0B2C9B28D0EA_dump4000Ev.root")                     
#fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/PhaseIITDRSpring19DR_Mu_FlatPt2to100_noPU_v31_E0D5C6A5-B855-D14F-9124-0B2C9B28D0EA_dump4000Ev.root")
##fileNames = cms.untracked.vstring("file:///pool/phedex/userstorage/carlosec/omtf/DisplacedMuonGun.root")
#fileNames = cms.untracked.vstring("file:///nfs/fanae/user/carlosec/OMTF_2020/samples/L1T-PhaseIITDRSpring19DR-00022_step1.root")
# fileNames = cms.untracked.vstring("/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/2AE8151D-FB68-9442-825F-7B56F033F675.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/63A6132F-1E36-5F45-885A-42196974F153.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/D6C64FD1-A305-3B4D-8E3F-79709311EED1.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/6FBC3497-36B1-AA4C-B4AD-F9B800891C76.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/0FC74B15-B121-8743-971C-0F74FE4597DD.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/A6320F29-8742-1E4D-8ED1-AC72238ED5B9.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/82B44A09-93B2-244D-B4E0-61A305DF07EE.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/B0339BC4-3A45-0246-8308-5FB4734CA9EF.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/DDB0C820-4E58-8B4E-AC04-071052A6802F.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/CA11401A-BF1C-354C-90F9-E60F311A03F4.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/14D38488-BEDF-CB4B-8932-1416DC58BB42.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/1083E314-BDC2-D242-8FDF-E0D0A5D77685.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/9967B524-1383-DC4F-8819-90F40DCE47AF.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/B8172E4F-9C69-1542-B61F-17BD1EA5F4FF.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/4093E0FA-B03A-0946-98D8-242B86BAE681.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/DFA26DCD-368D-0A42-8A38-BBE029E2D2F7.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/FDEE9C2F-1D31-0947-87D7-683B87A7D3BE.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/4C6DDED2-6250-E844-B964-1AA93A80CD12.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/933D45F7-BD41-8C40-AA35-E608B7049531.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/37DC07EF-F618-7E48-8B6E-7822479FF41B.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/0C24E4BA-D0F6-3242-AC82-49D8CD611F40.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/F4280E6F-B925-F641-8BA1-EEB874563AE5.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/DB328BF3-42F3-354A-A245-F859CE8C4632.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/9373B831-4B97-1B4B-8A5F-4E77EC50D2BE.root",
#"/store/mc/PhaseIITDRSpring19DR/DisplacedMuons_Pt30to100_Dxy0to3000-pythia8-gun/GEN-SIM-DIGI-RAW/NoPU_106X_upgrade2023_realistic_v3-v1/40000/E181816A-E10D-BF49-A906-1DC5A1AECA2F.root"),
)
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

process.simBayesOmtfDigis.lctCentralBx = cms.int32(8);#<<<<<<<<<<<<<<<<!!!!!!!!!!!!!!!!!!!!TODO this was changed in CMSSW 10(?) to 8. if the data were generated with the previous CMSSW then you have to use 6

process.simBayesOmtfDigisDisplaced = process.simBayesOmtfDigis.clone()
process.simBayesOmtfDigisDisplaced.patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0005_1.xml")

process.simBayesOmtfDigisBoth = process.simBayesOmtfDigis.clone()
process.simBayesOmtfDigisBoth.patternsXMLFiles = cms.VPSet( cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/PatternsDisplaced_0x0005_1.xml")), cms.PSet(patternsXMLFile = cms.FileInPath("L1Trigger/L1TMuon/data/omtf_config/Patterns_0x0003.xml")))

#process.simBayesOmtfDigis.goldenPatternResultFinalizeFunction = cms.int32(6) #valid values are 0, 1, 2, 3, 5, 6, but for other then 0 the candidates quality assignemnt must be updated

process.dumpED = cms.EDAnalyzer("EventContentAnalyzer")
process.dumpES = cms.EDAnalyzer("PrintEventSetupContent")

process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")

####Event Setup Producer
process.load("L1Trigger.L1TMuonOverlapPhase1.MuonMatcher_cfg")
process.load('Configuration.StandardSequences.MagneticField_cff')

process.dispSeq = cms.Sequence( process.dispGenEta
)

process.dispPath = cms.Path(process.dispSeq)


process.L1TMuonSeq = cms.Sequence( process.esProd          
                                   + process.simBayesOmtfDigis
		                   + process.simBayesOmtfDigisDisplaced 
                                   + process.simBayesOmtfDigisBoth
                                   + process.dispGenEta
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
