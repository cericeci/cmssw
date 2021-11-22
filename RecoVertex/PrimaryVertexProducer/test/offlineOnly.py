import FWCore.ParameterSet.Config as cms

process = cms.Process("PV")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun4_realistic_v3', '')

import FWCore.ParameterSet.VarParsing as VarParsing

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile = 'output.root'
options.inputFiles = ['input.root']
options.maxEvents = -1 # -1 means all events

options.register('seed',123456, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int)
options.seed = 123456
options.register( "firstRun",
                  1,  #default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,
                  "the first run"
                  )
options.register( "PU",
                  20,  #default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.float,
                  "Average pile up interactions"
                  )

options.parseArguments()
PU = options.PU
import os
files = tuple([ "file:/eos/user/c/cericeci/PV/QCD_%i/"%PU + f for f in os.listdir("/eos/user/c/cericeci/PV/QCD_%i/"%PU) ][0:1])

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(files),
    secondaryFileNames = cms.untracked.vstring()
)

process.out = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    outputCommands = cms.untracked.vstring( (
        'drop *', 'keep PileupSummaryInfos_*_*_*', 'keep recoVertexs_*_*_*', 'keep *_genParticles_*_*', 'keep *_pixelTracks_*_RECO')
    ),
    fileName = cms.untracked.string('offlineOnly%i_plustracks.root'%PU),
)

#process.Timing = cms.Service("Timing",
#  summaryOnly = cms.untracked.bool(False),
#  useJobReport = cms.untracked.bool(True)
#)


from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA
process.firstStepPrimaryVerticesUnsorted = SwitchProducerCUDA(

  cpu = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(12.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(1),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(0),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("pixelTracks","","RECO"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
  ),
  cuda = cms.EDProducer("PrimaryVertexProducerCUDA",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(12.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(1),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(0),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("pixelTracks","","RECO"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
  )
)
process.pv_step       = cms.Path(process.firstStepPrimaryVerticesUnsorted)
process.output_step = cms.EndPath(process.out)
#process.schedule = cms.Schedule(process.beamspot_step,process.cluster_step ,process.initial_step,process.pv_step,process.out)

