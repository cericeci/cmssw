from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'muCorr_MC_analysis_SingleNeutrino_PU200_mtd5_v1_t11'
#config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'runMuonOverlapTTMergerAnalyzerCrab.py'
config.JobType.psetName = 'runMuonCorrelatorTTTracksAnanlyzer_mtd5.py'
config.JobType.pyCfgParams = ['rate']

config.Data.inputDataset = '/NeutrinoGun_E_10GeV/PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2-v1/FEVT'
#config.Data.inputDataset = '/SingleNeutrino/PhaseIIFall17D-L1TPU200_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
#'/QCD_Pt-0to1000_Tune4C_14TeV_pythia8/PhaseIIFall17D-L1TPU200_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset = '/SingleMu_FlatPt-2to100/PhaseIIFall17D-L1TPU200_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset = '/SingleMu_FlatPt-2to100/PhaseIIFall17D-L1TnoPU_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 35
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_muCorr_MC_analysis_SingleNeutrino_PU200_mtd5_v1_t11'
config.Data.totalUnits = 2599  #1667 #75 600 total number is 1667
config.Data.ignoreLocality = False

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

config.Site.storageSite = 'T2_PL_Swierk'
#config.Site.whitelist = ['T2_US_Caltech', 'T3_US_Colorado']
#config.Site.blacklist = ['T2_US_Purdue', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin']
#does not work, so no matter