import FWCore.ParameterSet.Config as cms

process = cms.Process('TOPDQM')

## imports of standard configurations
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Services_cff')

## --------------------------------------------------------------------
## Frontier Conditions: (adjust accordingly!!!)
##
## For CMSSW_3_8_X MC use             ---> 'START38_V12::All'
## For Data (38X re-processing) use   ---> 'GR_R_38X_V13::All'
## For Data (38X prompt reco) use     ---> 'GR10_P_V10::All'
##
## For more details have a look at: WGuideFrontierConditions
## --------------------------------------------------------------------
##process.GlobalTag.globaltag = 'GR_R_42_V14::All' 
process.GlobalTag.globaltag = 'MCRUN2_74_V9'
#process.GlobalTag.globaltag = 'auto:startup_GRun'

#dbs search --query 'find file where site=srm-eoscms.cern.ch and dataset=/RelValTTbar/CMSSW_7_0_0_pre3-PRE_ST62_V8-v1/GEN-SIM-RECO'
#dbs search --query 'find dataset where dataset=/RelValTTbar/CMSSW_7_0_0_pre6*/GEN-SIM-RECO'

#/eos/cms/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/
#/eos/cms/store/relval/CMSSW_9_4_0/SingleMuon/DQMIO/94X_dataRun2_PromptLike_v5_RelVal_sigMu2017C-v1/10000/

## input file(s) for testing /SingleElectron/Run2016B-07Aug17_ver2-v2/AOD 
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("file:input.root',")
    fileNames = cms.untracked.vstring(
    #'/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/00B5B771-28D8-E711-8BFF-FA163ED9E97A.root'
    #Run 274199
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/108C5059-4FD1-E711-AE84-0025905B859E.root', 
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/448766CF-57D1-E711-9BD1-0025905A60EE.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/76EFC336-5DD1-E711-9B16-0CC47A4C8E66.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/A07D91AC-4DD1-E711-83D0-0025905A60B4.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/DAAD5D60-54D1-E711-8AEF-0CC47A7C3450.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/2402F2D9-89D1-E711-89B8-0CC47A78A456.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/48872150-59D1-E711-BB01-0025905A609A.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/7C31C6CC-63D1-E711-8C28-0CC47A7C35D8.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/B2A04A0C-64D1-E711-A4E3-0CC47A4D76C8.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/E660F9B5-53D1-E711-BD03-0025905A60FE.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/2655FD92-48D1-E711-93EF-0CC47A4D76B8.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/66868BD9-89D1-E711-91B4-0CC47A7C3458.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/8E6D0A6B-4CD1-E711-89F5-0CC47A78A426.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/C2C70ED7-48D1-E711-8905-0025905B85A2.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/E8F5385A-56D1-E711-8C92-0CC47A7C3408.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/30F3929C-65D1-E711-B347-0CC47A78A446.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/6A61D65F-66D1-E711-8B8C-0CC47A7C357E.root',
    #'/store/relval/CMSSW_9_4_0/SingleMuon/RAW-RECO/ZMu-94X_dataRun2_PromptLike_v9_RelVal_sigMu2016B-v1/10000/9EC3D350-5FD1-E711-B3F9-0025905A60EE.root',
    #RunB 2017
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/444DA4D2-3BA5-E711-A34C-48FD8EE73ACD.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/48037A22-70A5-E711-9952-0090FAA58C54.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/50D4505C-3BA5-E711-9353-48FD8EE73A8D.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/56640E5F-76A5-E711-ADA0-0090FAA57F34.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/5EE6F899-21A5-E711-850B-F02FA768CB48.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/7C328599-21A5-E711-9509-002590D0AFB6.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/BECBD924-70A5-E711-9D05-48FD8E2824C9.root',

    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/04AAE45F-12A8-E711-B4C8-FA163E18C131.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/0CCE5683-40A9-E711-8044-FA163EE1CC7E.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/308EF476-12A8-E711-A50D-02163E015124.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/4272A9CA-4EA9-E711-AAB9-FA163EB54E1B.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/5A020EB1-33A9-E711-B001-FA163E005C91.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/6C8B8C5A-12A8-E711-B8AA-FA163E5EC240.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/72B751D0-EBA7-E711-A201-FA163E1BBC68.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/72FB055C-12A8-E711-9960-FA163EB95E71.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/7C9E6386-40A9-E711-BDFA-FA163EF4B2DF.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/988A4558-12A8-E711-B46F-FA163E2E7F26.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/98F1EF8B-4EA9-E711-BE3D-FA163E7625E2.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/9AB4855A-12A8-E711-9C12-FA163E47539C.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/AAB10E6A-12A8-E711-9591-FA163ECA6A13.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/AEDF08FF-40A9-E711-AB19-02163E016557.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/B0ED02FF-40A9-E711-86DF-02163E016557.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/B60A1C7E-4EA9-E711-810F-02163E00BB2D.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/B8F20560-12A8-E711-B364-FA163EA5D320.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/C641D31B-18A8-E711-A21A-FA163E6FA9FE.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/C6FD935E-12A8-E711-9565-FA163E2E7F26.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/E6C667BF-4DA9-E711-A64B-FA163E8F7CB0.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10000/F6D927CB-40A9-E711-B08C-0025904B2C68.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/008DC132-5EA5-E711-AA12-0090FAA58224.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/06719922-70A5-E711-8614-0090FAA57470.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/0E0ACD3D-21A5-E711-A837-48D539D33367.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/1645FB22-70A5-E711-BAE2-48FD8E28246B.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/1C9B70AA-3AA5-E711-B1D6-48FD8EE739FF.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/2276A022-70A5-E711-A293-0090FAA57470.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/2485DF22-70A5-E711-B324-48D539F38632.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/42FFF622-70A5-E711-A5A0-48FD8E28246B.root',
    #'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/100000/4402A5B3-3BA5-E711-9E10-48FD8E282497.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/06C9A582-BBA9-E711-848E-FA163E7737A2.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/10C5AFBC-C6A9-E711-AF3F-FA163E7EABDD.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/1ACB3709-BFA9-E711-9FC6-02163E00ADD8.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/1E79C581-BBA9-E711-84A6-FA163EB815FA.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/22820569-C8A9-E711-AB3D-FA163EF52D13.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/2618BF5E-BBA9-E711-BB78-FA163ED191F5.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/2EC39128-BCA9-E711-8DE8-FA163EB815FA.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/4038AFB0-ADA9-E711-B287-02163E00B790.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/487DACBE-BEA9-E711-9E22-FA163E0683BD.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/543A2CE1-D0A9-E711-A0CB-FA163EF96018.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/7021D088-1EA9-E711-9B61-FA163E1004A1.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/7839A426-AAA9-E711-B305-FA163EA1FC8C.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/7A71624A-BBA9-E711-B018-FA163E7A2B5D.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/8CDA87FB-5FA9-E711-A0B9-FA163E497357.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/905688CD-ADA9-E711-9B6A-FA163EDA8F93.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/987240C9-ADA9-E711-AB1E-FA163EF52D13.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/B8DFB733-A3A9-E711-B875-FA163EDA8F93.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/CA8A567E-BBA9-E711-92D2-FA163E905947.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/CE01D122-AEA9-E711-896A-FA163E8F88D1.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/D00AC766-AAA9-E711-AADF-FA163ECB0D57.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/D65BFBD3-16A9-E711-A9EB-FA163E3E5663.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/EC522270-AAA9-E711-B621-02163E01516D.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/EE0D2FD0-ADA9-E711-9ED3-FA163E64C8B0.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/EEFA8ED3-ADA9-E711-87F5-FA163E18C131.root',
    'root://cms-xrd-global.cern.ch///store/data/Run2017B/SingleElectron/AOD/12Sep2017-v1/10001/FE7231AC-BEA9-E711-8B1F-02163E015FD9.root'
    #'/store/relval/CMSSW_9_4_0/RelValTTbarLepton_13/GEN-SIM-RECO/94X_mc2017_realistic_v10-v1/10000/545AE249-5DCA-E711-8BF2-0025905A6070.root',
    #'/store/relval/CMSSW_9_4_0/RelValTTbarLepton_13/GEN-SIM-RECO/94X_mc2017_realistic_v10-v1/10000/56A9CA8C-5ECA-E711-A4F9-0025905A610A.root',
    #'/store/relval/CMSSW_9_4_0/RelValTTbarLepton_13/GEN-SIM-RECO/94X_mc2017_realistic_v10-v1/10000/6C27A566-5CCA-E711-AF43-0CC47A7C34EE.root',
    #'/store/relval/CMSSW_9_4_0/RelValTTbarLepton_13/GEN-SIM-RECO/94X_mc2017_realistic_v10-v1/10000/EC906088-5ECA-E711-A1D6-0CC47A78A340.root'
    ),
)

## number of events
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(1000000)
)

## apply VBTF electronID (needed for the current implementation
## of topSingleElectronDQMLoose and topSingleElectronDQMMedium)
#process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("DQM.Physics.topElectronID_cff")
process.load('Configuration/StandardSequences/Reconstruction_cff')


## output
process.output = cms.OutputModule("PoolOutputModule",
  fileName       = cms.untracked.string('topDQM_production_El.root'),
  outputCommands = cms.untracked.vstring(
    'drop *_*_*_*',
    'keep *_*_*_TOPDQM',
    'drop *_TriggerResults_*_TOPDQM',
    'drop *_simpleEleId70cIso_*_TOPDQM'
  ),
  splitLevel     = cms.untracked.int32(0),
  dataset = cms.untracked.PSet(
    dataTier   = cms.untracked.string(''),
    filterName = cms.untracked.string('')
  )
)

## load jet corrections
process.load("JetMETCorrections.Configuration.JetCorrectors_cff")

## check the event content
process.content = cms.EDAnalyzer("EventContentAnalyzer")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('TopSingleLeptonDQM'   )
process.MessageLogger.cerr.TopSingleLeptonDQM    = cms.untracked.PSet(limit = cms.untracked.int32(1))
process.MessageLogger.categories.append('TopDiLeptonOfflineDQM')
process.MessageLogger.cerr.TopDiLeptonOfflineDQM = cms.untracked.PSet(limit = cms.untracked.int32(1))
process.MessageLogger.categories.append('SingleTopTChannelLeptonDQM'   )
process.MessageLogger.cerr.SingleTopTChannelLeptonDQM    = cms.untracked.PSet(limit = cms.untracked.int32(1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MEtoEDMConverter.deleteAfterCopy = cms.untracked.bool(False)  ## line added to avoid crash when changing run number


process.load("DQM.Physics.topSingleLeptonDQM_cfi")
process.load("DQM.Physics.singleTopDQM_cfi")


## path definitions
process.p      = cms.Path(
#    process.simpleEleId70cIso          *
    #process.DiMuonDQM                  +
    #process.DiElectronDQM              +
    #process.ElecMuonDQM                +
    #process.topSingleMuonLooseDQM      +
    process.ak4PFCHSL1FastL2L3CorrectorChain * process.topSingleMuonMediumDQM     +
    #process.topSingleElectronLooseDQM  +
    process.ak4PFCHSL1FastL2L3CorrectorChain * process.topSingleElectronMediumDQM +
    process.ak4PFCHSL1FastL2L3CorrectorChain * process.singleTopMuonMediumDQM      +
    process.ak4PFCHSL1FastL2L3CorrectorChain * process.singleTopElectronMediumDQM
)
process.endjob = cms.Path(
    process.endOfProcess
)
process.fanout = cms.EndPath(
    process.output
)

## schedule definition
process.schedule = cms.Schedule(
    process.p,
    process.endjob,
    process.fanout
)
