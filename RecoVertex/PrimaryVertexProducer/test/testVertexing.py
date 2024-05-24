import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('PV',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2023_realistic_v3')

# Input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/2af100a0-34ce-4b20-8e3e-399fc84d79ea.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/cf90c900-77b4-49b5-97e8-0ce5582edc3c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/2b8e6757-88ec-48b0-9222-21c53d44b596.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7016b175-1b1e-4604-ae59-bc68a73f184c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e11d04a4-c0ab-4e22-aeef-c72faf7a1a16.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/fbe4b36c-e04a-49f0-8458-82df6cefbe7b.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3148eca3-9e23-4f48-b2d1-7600025bde47.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/01e1f85f-a402-4cb1-ae45-84a772246746.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/20a5f1cc-7afe-404c-b3cd-ba9d626d8eef.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/08a6ec05-b8f1-4a4d-8093-f754d8d8ea6a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/72b9f410-164e-4792-ab17-4f730a883ef9.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/ee64ae6b-1928-4c3f-96d3-f670f5d8c372.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3e51b971-a3d6-4b4b-a68f-f8b9f2b5701c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/0692318b-1599-452d-b903-d2dfb434481f.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/5c4c726f-0101-496e-966f-90e30244b559.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3207151f-0064-4ee8-8d6b-e2ddb541d318.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c11f1a13-47e7-45ff-b4e1-9885bdd7a386.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9ce0610d-c810-4df5-aa87-7ab3242e6385.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/2117deba-4d15-4af5-b6f3-51b7599910e5.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/676aca18-0631-460b-ae8f-3c333ed3a637.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/fd7508f7-392e-480e-87a6-eecaf8908126.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e53d0133-7375-46c5-9fa2-6241dd298a2b.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/5dcd5c62-866a-44d9-a006-cb2dec67a6cc.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/01ce86e5-acc5-4316-8ede-2889ad4af564.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/62321fb1-ff98-48a5-bbb1-22a4c8f898f6.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/71cd17cc-eb65-4785-ae33-512ebea26275.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/770ca919-08d3-42b1-808d-34bdbfbb9bfa.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/cbe27d8f-a4da-4dbd-9e05-92b7bfb59eb9.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e423235f-a368-40c3-87b7-39a0e479566a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/33b9e593-fbdf-422a-a5d0-59f62332c838.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d4f20e92-06a3-4f34-9e17-7b0735d49f71.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/983af0ec-2fa7-4992-bf26-cd9ec4246338.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/88f0985e-6e0c-469d-b42f-dba5984b4f4b.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/18d0b568-ffb9-42ea-988e-d3c7bd169326.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/f5bcec48-c44f-497f-a3e5-b483e654da96.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/71edd45c-b0ed-4a2b-9ea4-098e232c475f.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7d21bee7-c044-466d-b9f3-b9ad647baefa.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/135332da-ffc7-43f9-89ba-c187ce5191f4.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/5905906c-ab6e-4ea8-939d-310b90e7407a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/a453f765-9df0-4cb8-8345-d3eacc31f9f1.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/367293c6-68fa-49fb-8ac4-41133f99dfed.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/b3300f52-fedf-4ce1-b90b-db06b9b14a3d.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/f19610b1-7445-468f-a455-478e58b40e32.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/39064eea-8043-4391-b9ed-fc3d3997996d.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/470a915c-254e-4bb6-adc1-c4513db1bfdc.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/53ff6b7d-2f5c-44b5-b6cf-bc183a17c642.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/08be49d6-4108-4a07-8581-8614ecbfcfad.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/82d9ba6e-8981-463b-ac66-711d3e4a3afe.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/79bca282-04bf-4257-ad08-f1aa8e72b1e7.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/90055548-31d7-42e7-bc56-3aea0ffd5abe.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9dec55d8-3321-452f-ab53-338edfa54931.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c07a12f7-bf6b-40d4-8cb7-51ebc79c3854.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d1bc040f-5c53-4618-a181-ed2b54bb54bf.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d88e3a10-215e-4c8c-9f81-d833ab8ecca1.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/685261d3-f32f-4063-ac94-16c3c1bab9b7.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/841611ba-3303-4f65-80f4-cd3ecfc970dd.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c3e32238-9d2c-4b52-990b-aa7f87beef99.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/65cc6f7f-2d2c-4dec-8681-08031e44387a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e6095cb5-d1ea-4208-8075-bfe225ffdeeb.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/5800f561-7ce2-4612-b43e-37f676039a4b.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/33feef8e-5994-49c9-8aa5-5b3c53f2d542.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/6700f8da-f498-4977-8966-b7a6f697d6b8.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/444b6495-9c02-4a51-922c-0fb59dfb50a3.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d9f98b7b-3e98-47e3-ad3b-727d03dfbfc8.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d6579ece-9dee-429f-a6ef-7d9b53883860.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3169feb4-3666-40fa-bf7c-899516400234.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/ed6a4538-f6f3-4c3f-b615-2e41dc18bb45.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/025b9ad2-d596-4308-bcf9-dd31a26c5a3c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/bdf9d912-d34d-45b6-9826-41a260f4c32c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/065b49df-ae79-4b95-9cef-ad2a4b119bd4.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/032e8f59-69dc-4a76-9363-67fb2d8bb6ec.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3e49a72e-5720-41b5-ae2d-e0ab95d84138.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/08f3448b-2acf-4bd1-ae2f-9eead0938d71.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7e1885a5-f578-4220-8bb9-bb7591e8821d.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/29ac239d-d829-4a12-b607-c90dc0a875e7.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/46b20c8b-0979-4d1e-b2a5-2ad0405c27aa.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/475df9f2-3f69-4a82-ac6b-f98a5df5d922.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/93089dc2-5fbe-4925-be75-0dc7fe8b7714.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c4f5767b-65a4-42f3-adc0-6ee423cce690.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/cbf2307a-8510-4922-bfa1-fb5277ba0138.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/1aa4347a-8f18-4207-962b-05f5735339d0.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/07d2ab0f-7f6a-45b6-97b2-12bfdaf1d70a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/dec993c6-367c-4ea9-ad97-ff3e4a6da41a.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/4a7cc722-a12d-423c-9264-778cc7c2b42e.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/b645d6c8-9d8b-4e3e-8373-f2aa7525d57e.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/824e763f-a5eb-466b-be9b-99e09e2ec16f.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/97fad9cd-18db-4762-9de8-51153db17997.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e5b74e6d-e986-435e-b81e-8fa7203ff8bc.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9e23424e-e69a-4d3d-88a8-621e6bf2aea3.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7b420b48-2257-44b8-9932-6614c814b586.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c8237e0f-1d4f-4e4b-b203-6215e854bbbb.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/8ce2d0ca-ec08-48e2-b539-15c7c82bee86.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c6c256e5-051e-4989-898d-f08f6b5eb459.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/f1735c59-6cf6-4b94-964e-ca251bb3d211.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/b4f031db-5997-4257-a6cb-bf4db08f59ec.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/6f13f183-ae25-4a5b-949c-84dc0a41f20d.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/83da07ab-63a1-4013-811b-ceac950da943.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c3fadbe0-f3db-4738-91c3-981e5261c1b7.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/307c7086-8960-4106-afe4-880d90282589.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/53019a57-c8bc-4692-a0f0-72414174cfcd.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/be76d5d5-2bd9-4f35-80ba-4aabc57957ed.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/bd06107b-24e6-4d2b-a242-ba0f71ae7701.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/3aca2c2e-7220-40fa-9451-3eba61ce48db.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/ed2f254c-8308-4927-bb8b-49eef8f6c4e9.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/ad89745e-3558-4f73-b43c-66674279044e.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9e11ba43-3fa6-4a93-a077-dc3d29646988.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/38389183-24b0-4b54-8e74-9e967c78a402.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/e8a311d0-fa5f-46db-b053-8b5a3dbcc2e6.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/d9375ee7-a042-46e4-adda-01b23d30c682.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c376cc9c-69bf-4f29-978f-1d5cc814f2bf.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/50705f35-d544-430b-bea0-a0003f40cc93.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/55231b77-da83-4ab3-9fd8-339c7e854855.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/fe3975d7-6398-4b0c-b710-e3ba665e3aca.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/43ea7f36-bb4e-4fb4-9ab2-97fe78e1c34e.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7fe6f6c6-5dcf-4c7d-ae26-d9c1f27c15b9.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/435534ca-66c8-420f-b7eb-512400117ee4.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/090a5d34-e4a0-4a8f-a62c-7fc18494264f.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7c4f7981-2b8f-4e54-9503-c04eaa9024ee.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/71a704ec-6fda-459b-b3f0-7f9d36f48cf3.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/c4b7deca-24ff-4a46-acb1-828d723ecb08.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/7f2ca577-7ab9-465b-8d79-15e62b89ff5c.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/442d0f93-b006-4e4b-bff4-3be4d9450f51.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/136d65f4-2d59-4626-a7cc-b12fab3682ff.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/971673f6-7ef6-4c08-b7ad-e10eed2fcb34.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/0bace915-648b-408d-89ba-f94f49d6f40f.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9959545a-be6c-44ac-9e35-1a1a60231023.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/9b455410-395c-4612-94f7-8032fec4eda8.root',
        '/store/relval/CMSSW_14_0_0/RelValTTbarToDilepton_14TeV/GEN-SIM-RECO/PU_140X_mcRun4_realistic_v1_STD_2026D98_PU-v1/2580000/156965ca-bad3-4177-80f4-11d93661fd3e.root'
    ),
    secondaryFileNames = cms.untracked.vstring(),
)


import sys
import argparse
parser = argparse.ArgumentParser(prog=f"{sys.argv[0]} {sys.argv[1]} --", description='Test and validation of PrimaryVertexProducer')
parser.add_argument('-a', '--algo', type=str, default='old', help='Whether to run the old or new algorithm')
parser.add_argument('-o', '--output', type=str, default='testPV.root', help='Output file name for main file (DQM file will be the same ending in _dqm.root')
parser.add_argument('-d', '--dqm', default=False, action="store_true", help='If activated, run and save DQM plots')
parser.add_argument('-n', '--nevents', default=-1, type=int, help='How many events to run (default is -1, meaning all of them)')
args = parser.parse_args()


# Number of events to run
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(args.nevents),
)

# Production metadata
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PV nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)


# Output definition
process.FEVToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(args.output), # output file name
    outputCommands = cms.untracked.vstring('drop *','keep *_*_*_PV', 'keep *_genPUProtons_*_*'),# I.e., just drop everything and keep things in this module
    splitLevel = cms.untracked.int32(0)
)

# Endpath and output
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVToutput_step = cms.EndPath(process.FEVToutput)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)


################################
## Now the plugins themselves ##
################################


from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices

process.offlinePrimaryVertices = offlinePrimaryVertices
process.offlinePrimaryVertices.TkClusParameters.TkDAClusParameters.runInBlocks = cms.bool(True if args.algo == "new" else False)
process.offlinePrimaryVertices.TkClusParameters.TkDAClusParameters.block_size = cms.uint32(512)
process.offlinePrimaryVertices.TkClusParameters.TkDAClusParameters.overlap_frac = cms.double(0.5)
process.offlinePrimaryVertices.vertexCollections = cms.VPSet(
       [cms.PSet(label=cms.string(""),
           algorithm=cms.string("WeightedMeanFitter" if args.algo == "new" else "AdaptiveVertexFitter"),
           chi2cutoff = cms.double(2.5),
           minNdof=cms.double(0.0),
           useBeamConstraint = cms.bool(False),
           maxDistanceToBeam = cms.double(1.0)
        ),
           cms.PSet(label=cms.string("WithBS"),
            algorithm = cms.string("WeightedMeanFitter" if args.algo == "new" else "AdaptiveVertexFitter"),
            minNdof=cms.double(0.0),
            chi2cutoff = cms.double(2.5),
            useBeamConstraint = cms.bool(True),
            maxDistanceToBeam = cms.double(1.0)
        )])

# Timing module #
process.ThroughputService = cms.Service('ThroughputService',
        eventRange = cms.untracked.uint32(10),
        eventResolution = cms.untracked.uint32(1),
        printEventSummary = cms.untracked.bool(True),
        enableDQM = cms.untracked.bool(True),
        dqmPathByProcesses = cms.untracked.bool(False),
        dqmPath = cms.untracked.string('Throughput'),
        timeRange = cms.untracked.double(1000),
        timeResolution = cms.untracked.double(1)
)

process.MessageLogger.cerr.ThroughputService = cms.untracked.PSet(
        limit = cms.untracked.int32(10000000)
)

process.options.wantSummary = True

###################################
## Last, organize paths and exec ##
###################################
if args.DQM: # If we run DQM we need some more things
  process.load('commons_cff')
  ##DQM Output step
  process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:%s'%(args.output.replace(".root","_DQM.root"))),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
  )

  process.vertexAnalysis.vertexRecoCollections= cms.VInputTag("offlinePrimaryVertices")
  process.pvMonitor.vertexLabel = cms.InputTag("offlinePrimaryVertices")

  process.tracksValidationTruth = cms.Task(process.VertexAssociatorByPositionAndTracks, process.quickTrackAssociatorByHits, process.tpClusterProducer)
  process.pvValidation = cms.Sequence(process.vertexAnalysis,process.tracksValidationTruth)
  process.prevalidation_step = cms.Path(process.pvValidation)

  process.DQMOfflineVertex = cms.Sequence(process.pvMonitor)
  process.dqmoffline_step = cms.EndPath(process.DQMOfflineVertex)
  process.DQMoutput_step = cms.EndPath(process.DQMoutput)
  process.vertexAnalysis.nPUbins = cms.uint32(200)

  process.vertexing_task = cms.EndPath(process.offlinePrimaryVertices)
  process.schedule = cms.Schedule(process.vertexing_task,process.prevalidation_step,process.dqmoffline_step,process.DQMoutput_step)
  process.schedule.extend([process.endjob_step,process.FEVToutput_step])


else:
  process.vertexing_task = cms.EndPath(process.offlinePrimaryVertices)
  process.schedule = cms.Schedule(process.vertexing_task)
  process.schedule.extend([process.endjob_step,process.FEVToutput_step])
