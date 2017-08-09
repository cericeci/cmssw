import FWCore.ParameterSet.Config as cms

#Primary vertex selection
PVCut = "abs(z) < 24. & position.rho < 2. & ndof > 4 & !isFake"

#Jet selection
looseJetCut = "(chargedHadronEnergyFraction()>0 && chargedMultiplicity()>0 && chargedEmEnergyFraction()<0.99 && neutralHadronEnergyFraction()<0.99 && neutralEmEnergyFraction()<0.99 && (chargedMultiplicity()+neutralMultiplicity())>1) && abs(eta)<=2.4 "

tightJetCut = "(chargedHadronEnergyFraction()>0 && chargedMultiplicity()>0 && chargedEmEnergyFraction()<0.99 && neutralHadronEnergyFraction()<0.90 && neutralEmEnergyFraction()<0.90 && (chargedMultiplicity()+neutralMultiplicity())>1) && abs(eta)<=2.4 "

#Loose muon selection
looseMuonCut  = "(muonRef.isNonnull && (muonRef.isGlobalMuon || muonRef.isTrackerMuon) && muonRef.isPFMuon)"
looseIsoCut   = "((muonRef.pfIsolationR04.sumChargedHadronPt + max(0., muonRef.pfIsolationR04.sumNeutralHadronEt + muonRef.pfIsolationR04.sumPhotonEt - 0.5 * muonRef.pfIsolationR04.sumPUPt) ) / muonRef.pt < 0.25)"
#Medium muon selection. Also requires either good global muon or tight segment compatibility
mediumMuonCut = looseMuonCut + " muonRef.innerTrack.validFraction > 0.8"

#Tight muon selection. Lacks distance to primary vertex variables, dz<0.5, dxy < 0.2. Now done at .cc
tightMuonCut  = "muonRef.isNonnull && muonRef.isGlobalMuon && muonRef.isPFMuon && muonRef.globalTrack.normalizedChi2 < 10. && muonRef.globalTrack.hitPattern.numberOfValidMuonHits > 0 && " + \
               "muonRef.numberOfMatchedStations > 1 && muonRef.innerTrack.hitPattern.numberOfValidPixelHits > 0 && muonRef.innerTrack.hitPattern.trackerLayersWithMeasurement > 5 "
tightIsoCut   = "(muonRef.pfIsolationR04.sumChargedHadronPt + max(0., muonRef.pfIsolationR04.sumNeutralHadronEt + muonRef.pfIsolationR04.sumPhotonEt - 0.5 * muonRef.pfIsolationR04.sumPUPt) ) / muonRef.pt < 0.15"

#Electron isolation selections
looseEleCut = "((gsfElectronRef.full5x5_sigmaIetaIeta() < 0.011 && gsfElectronRef.superCluster().isNonnull() && gsfElectronRef.superCluster().seed().isNonnull() && (gsfElectronRef.deltaEtaSuperClusterTrackAtVtx() - gsfElectronRef.superCluster().eta() + gsfElectronRef.superCluster().seed().eta()) < 0.00477 && abs(gsfElectronRef.deltaPhiSuperClusterTrackAtVtx()) < 0.222 && gsfElectronRef.hadronicOverEm() < 0.298 && abs(1.0 - gsfElectronRef.eSuperClusterOverP())*1.0/gsfElectronRef.ecalEnergy() < 0.241 && gsfElectronRef.gsfTrack.hitPattern().numberOfHits('MISSING_INNER_HITS') <= 1 && abs(gsfElectronRef.eta) < 1.479) ||  (gsfElectronRef.full5x5_sigmaIetaIeta() < 0.0314 && gsfElectronRef.superCluster().isNonnull() && gsfElectronRef.superCluster().seed().isNonnull() && (gsfElectronRef.deltaEtaSuperClusterTrackAtVtx() - gsfElectronRef.superCluster().eta() + gsfElectronRef.superCluster().seed().eta()) < 0.00868 && abs(gsfElectronRef.deltaPhiSuperClusterTrackAtVtx()) < 0.213 && gsfElectronRef.hadronicOverEm() < 0.101  && abs(1.0 - gsfElectronRef.eSuperClusterOverP())*1.0/gsfElectronRef.ecalEnergy() < 0.14 && gsfElectronRef.gsfTrack.hitPattern().numberOfHits('MISSING_INNER_HITS') <= 1 && abs(gsfElectronRef.eta) > 1.479))"

#Redefined on .cc
#ElelooseIsoCut  = "(((gsfElectronRef.pfIsolationVariables.sumChargedHadronPt + max(0., gsfElectronRef.pfIsolationVariables.sumNeutralHadronEt + gsfElectronRef.pfIsolationVariables.sumPhotonEt - 0.5 * gsfElectronRef.pfIsolationVariables.sumPUPt) ) / gsfElectronRef.pt < 0.0994 && abs(gsfElectronRef.eta) < 1.479) || ((gsfElectronRef.pfIsolationVariables.sumChargedHadronPt + max(0., gsfElectronRef.pfIsolationVariables.sumNeutralHadronEt + gsfElectronRef.pfIsolationVariables.sumPhotonEt - 0.5 * gsfElectronRef.pfIsolationVariables.sumPUPt) ) / gsfElectronRef.pt < 0.107 && abs(gsfElectronRef.eta) > 1.479))"

tightEleCut = "((gsfElectronRef.full5x5_sigmaIetaIeta() < 0.00998 && gsfElectronRef.superCluster().isNonnull() && gsfElectronRef.superCluster().seed().isNonnull() && (gsfElectronRef.deltaEtaSuperClusterTrackAtVtx() - gsfElectronRef.superCluster().eta() + gsfElectronRef.superCluster().seed().eta()) < 0.00308  && abs(gsfElectronRef.deltaPhiSuperClusterTrackAtVtx()) < 0.0816 && gsfElectronRef.hadronicOverEm() < 0.0414 && abs(1.0 - gsfElectronRef.eSuperClusterOverP())*1.0/gsfElectronRef.ecalEnergy() < 0.0129 && gsfElectronRef.gsfTrack.hitPattern().numberOfHits('MISSING_INNER_HITS') <= 1 && abs(gsfElectronRef.eta) < 1.479) ||  (gsfElectronRef.full5x5_sigmaIetaIeta() < 0.0292 && gsfElectronRef.superCluster().isNonnull() && gsfElectronRef.superCluster().seed().isNonnull() && (gsfElectronRef.deltaEtaSuperClusterTrackAtVtx() - gsfElectronRef.superCluster().eta() + gsfElectronRef.superCluster().seed().eta()) < 0.00605 && abs(gsfElectronRef.deltaPhiSuperClusterTrackAtVtx()) < 0.0394  && gsfElectronRef.hadronicOverEm() < 0.0641  && abs(1.0 - gsfElectronRef.eSuperClusterOverP())*1.0/gsfElectronRef.ecalEnergy() <	0.0129 && gsfElectronRef.gsfTrack.hitPattern().numberOfHits('MISSING_INNER_HITS') <= 1 && abs(gsfElectronRef.eta) > 1.479))"

#Redefined on .cc
#EletightIsoCut  = "(((gsfElectronRef.pfIsolationVariables.sumChargedHadronPt + max(0., gsfElectronRef.pfIsolationVariables.sumNeutralHadronEt + gsfElectronRef.pfIsolationVariables.sumPhotonEt - 0.5 * gsfElectronRef.pfIsolationVariables.sumPUPt) ) / gsfElectronRef.pt < 0.0588 && abs(gsfElectronRef.eta) < 1.479) || ((gsfElectronRef.pfIsolationVariables.sumChargedHadronPt + max(0., gsfElectronRef.pfIsolationVariables.sumNeutralHadronEt + gsfElectronRef.pfIsolationVariables.sumPhotonEt - 0.5 * gsfElectronRef.pfIsolationVariables.sumPUPt) ) / gsfElectronRef.pt < 0.0571 && abs(gsfElectronRef.eta) > 1.479))"


topSingleLeptonDQM = cms.EDAnalyzer("TopSingleLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit 
    ## communication to TopCom!
    directory = cms.string("Physics/Top/TopSingleLeptonDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")
    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string("abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake")
    ),
    ## [optional] : when omitted all monitoring plots for electrons
    ## will be filled w/o extras
    elecExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o cut on electronId
      ##electronId = cms.PSet( src = cms.InputTag("mvaTrigV0"), cutValue = cms.double(0.5) ),
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the electron candidates                                                                                            
      select = cms.string("pt>15 & abs(eta)<2.5 & abs(gsfTrack.d0)<1 & abs(gsfTrack.dz)<20"),
      ## when omitted isolated electron multiplicity plot will be equi-
      ## valent to inclusive electron multiplicity plot 
      #isolation = cms.string(ElelooseIsoCut),
			rho = cms.InputTag("fixedGridRhoFastjetAll"),
    ),
    ## [optional] : when omitted all monitoring plots for muons
    ## will be filled w/o extras
    muonExtras = cms.PSet(
      ## when omitted muon plots will be filled w/o additional pre-
      ## selection of the muon candidates                                                                                            
      select = cms.string(looseMuonCut + " && pt>10 & abs(eta)<2.4"),
      ## when omitted isolated muon multiplicity plot will be equi-
      ## valent to inclusive muon multiplicity plot                                                    
      isolation = cms.string(looseIsoCut),
    ),
    ## [optional] : when omitted all monitoring plots for jets will
    ## be filled from uncorrected jets
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets                                            
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      ## when omitted monitor plots will be filled w/o additional cut on
      ## jetID                                                   
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
#      ),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets
      select = cms.string("pt>30 & abs(eta)<2.4 "),
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass befor filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    triggerExtras = cms.PSet(
      src   = cms.InputTag("TriggerResults","","HLT"),
      paths = cms.vstring(['HLT_Mu3:HLT_QuadJet15U',
                           'HLT_Mu5:HLT_QuadJet15U',
                           'HLT_Mu7:HLT_QuadJet15U',
                           'HLT_Mu9:HLT_QuadJet15U'])
    )                                            
  ),                                  
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    ## [optional] : when omitted no preselection is applied
    #trigger = cms.PSet(
    #  src    = cms.InputTag("TriggerResults","","HLT"),
    #  select = cms.vstring(['HLT_Mu11', 'HLT_Ele15_LW_L1R', 'HLT_QuadJet30'])
    #),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string('abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake')
    )                                        
  ),  
  ## ------------------------------------------------------    
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  ##    
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("jets/pf:step0"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
 #     ),
      min = cms.int32(2),
    ),
  )
)

topSingleMuonLooseDQM = cms.EDAnalyzer("TopSingleLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("Physics/Top/TopSingleMuonLooseDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")
    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string("abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake")
    ),
    ## [optional] : when omitted all monitoring plots for muons
    ## will be filled w/o extras                                           
    muonExtras = cms.PSet(
      ## when omitted muon plots will be filled w/o additional pre-
      ## selection of the muon candidates                                                                                               
      select = cms.string(looseMuonCut + " && pt > 10 & abs(eta)<2.4"),
      ## when omitted isolated muon multiplicity plot will be equi-
      ## valent to inclusive muon multiplicity plot                                                    
      isolation = cms.string(looseIsoCut)                                               
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets                                               
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      ## when omitted monitor plots will be filled w/o additional cut on
      ## jetID                                                                                                                     
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
  #    ),                                                    
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets                                                
      select = cms.string("pt>30 & abs(eta)<2.4"),
      ## when omitted monitor histograms for b-tagging will not be filled 
      jetBTaggers  = cms.PSet(
		cvsVertex = cms.PSet(
          label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
	          workingPoint = cms.double(0.970)
	          # CSV Tight from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation74X
        )
      ),                                                
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass befor filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    triggerExtras = cms.PSet(
      src   = cms.InputTag("TriggerResults","","HLT"),
      paths = cms.vstring(['HLT_Mu3:HLT_QuadJet15U',
                           'HLT_Mu5:HLT_QuadJet15U',
                           'HLT_Mu7:HLT_QuadJet15U',
                           'HLT_Mu9:HLT_QuadJet15U',
                           'HLT_Mu11:HLT_QuadJet15U'])
    )
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    ## [optional] : when omitted no preselection is applied
    #trigger = cms.PSet(
    #  src    = cms.InputTag("TriggerResults","","HLT"),
    #  select = cms.vstring(['HLT_Mu11'])
    #),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string('abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake')
    )
  ),
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("muons:step0"),
      src    = cms.InputTag("pfIsolatedMuonsEI"),
      select = cms.string(looseMuonCut + looseIsoCut + " && pt>10 & abs(eta)<2.4"), # CB what about iso? CD Added looseIso
      min    = cms.int32(1),
    ),
    cms.PSet(
      label  = cms.string("jets/pf:step1"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      #select = cms.string("pt>30 & abs(eta)<2.5 & emEnergyFraction>0.01"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
   #   ),
      min = cms.int32(1),                                               
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step2"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
    #  ),
      min = cms.int32(2),                                               
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step3"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
     # ),
      min = cms.int32(3),                                               
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step4"),
      src    = cms.InputTag("pfMet"),
      select = cms.string("pt>30"),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
			#),
      #min = cms.int32(4),                                               
    ), 
  )
)

topSingleMuonMediumDQM = cms.EDAnalyzer("TopSingleLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("Physics/Top/TopSingleMuonMediumDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")

    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string(PVCut)
    ),
    ## [optional] : when omitted all monitoring plots for muons
    ## will be filled w/o extras                                           
    muonExtras = cms.PSet(
      ## when omitted muon plots will be filled w/o additional pre-
      ## selection of the muon candidates                                                
      select    = cms.string(looseMuonCut + " && pt>20 & abs(eta)<2.1"),  
      ## when omitted isolated muon multiplicity plot will be equi-
      ## valent to inclusive muon multiplicity plot                                                    
      isolation = cms.string(looseIsoCut)
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      ## when omitted monitor plots will be filled w/o additional cut on
      ## jetID                                                                                                   
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
 #     ),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets                                                
      select = cms.string("pt>30 & abs(eta)< 2.4 & " + looseJetCut),
      ## when omitted monitor histograms for b-tagging will not be filled                                                                                                   
      jetBTaggers  = cms.PSet(
		cvsVertex = cms.PSet(
          label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
	          workingPoint = cms.double(0.970)
	          # CSV Tight from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation74X
        )
      ),                                                                                                
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass before filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
#    triggerExtras = cms.PSet(
#      src   = cms.InputTag("TriggerResults","","HLT"),
#     paths = cms.vstring(['HLT_Mu3:HLT_QuadJet15U',
#                          'HLT_Mu5:HLT_QuadJet15U',
#                          'HLT_Mu7:HLT_QuadJet15U',
#                          'HLT_Mu9:HLT_QuadJet15U',
#                          'HLT_Mu11:HLT_QuadJet15U'])      
#    )
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    ## [optional] : when omitted no preselection is applied
    #trigger = cms.PSet(
    #  src    = cms.InputTag("TriggerResults","","HLT"),
    #  select = cms.vstring(['HLT_Mu15_v2'])
    #),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string(PVCut)
    )
  ),
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("muons:step0"),
      src    = cms.InputTag("pfIsolatedMuonsEI"),
      select = cms.string(tightMuonCut +"&&"+ tightIsoCut + " && pt>20 & abs(eta)<2.1"), # CB what about iso? CD Added tightIso      
      min    = cms.int32(1),
      max    = cms.int32(1),
    ),
    cms.PSet(
      label  = cms.string("jets/pf:step1"),
      #src    = cms.InputTag("ak4PFJetsCHS"),
      src    = cms.InputTag("ak4PFJetsCHS"),
			#jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      #select = cms.string("pt>30 & abs(eta)<2.5 & emEnergyFraction>0.01"),
      select = cms.string("pt>30 & abs(eta)<2.4 & "+ looseJetCut),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
  		#),
      min = cms.int32(4),
    ), 
    cms.PSet(
      label  = cms.string("met/pf:step2"),
      src    = cms.InputTag("pfMet"),
      #jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30"),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
#      ),
#      min = cms.int32(1),                                                
    ),
  )
)

topSingleElectronLooseDQM = cms.EDAnalyzer("TopSingleLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("Physics/Top/TopSingleElectronLooseDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")

    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select = cms.string("abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake")
    ),
    ## [optional] : when omitted all monitoring plots for electrons
    ## will be filled w/o extras
    elecExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o cut on electronId
      #electronId = cms.PSet( src = cms.InputTag("mvaTrigV0"), cutValue = cms.double(0.0) ),
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the electron candidates
      select     = cms.string("pt>20 & abs(eta)<2.5"),
      ## when omitted isolated electron multiplicity plot will be equi-
      ## valent to inclusive electron multiplicity plot                                                    
      #isolation  = cms.string(ElelooseIsoCut),                                                   
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      ## when omitted monitor plots will be filled w/o additional cut on
      ## jetID                                                   
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
    #  ),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets
      #select = cms.string("pt>30 & abs(eta)<2.5 & emEnergyFraction>0.01"), 
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      ## when omitted monitor histograms for b-tagging will not be filled                                                   
      jetBTaggers  = cms.PSet(
		cvsVertex = cms.PSet(
          label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
	          workingPoint = cms.double(0.970)
	          # CSV Tight from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation74X
        )
      ),                                                
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass before filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    triggerExtras = cms.PSet(
      src   = cms.InputTag("TriggerResults","","HLT"),
      paths = cms.vstring(['HLT_Ele15_LW_L1R:HLT_QuadJetU15'])
    )
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    ## [optional] : when omitted no preselection is applied
    #trigger = cms.PSet(
    #  src    = cms.InputTag("TriggerResults","","HLT"),
    #  select = cms.vstring(['HLT_Ele15_SW_CaloEleId_L1R'])
    #),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string('abs(x)<1. & abs(y)<1. & abs(z)<20. & tracksSize>3 & !isFake')
    )
  ),
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label  = cms.string("elecs:step0"),
      src    = cms.InputTag("pfIsolatedElectronsEI"),
      select = cms.string("pt>20 & abs(eta)<2.5 "),
      min    = cms.int32(1),
    ),
    cms.PSet(
      label  = cms.string("jets/pf:step1"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
     # ),
      min = cms.int32(1),                                                   
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step2"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
#      ),
      min = cms.int32(2),
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step3"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
 #     ),
      min = cms.int32(3),
    ), 
    cms.PSet(
      label  = cms.string("jets/pf:step4"),
      src    = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 "),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
  #    ),
      min = cms.int32(4),
    ),
  )
)

topSingleElectronMediumDQM = cms.EDAnalyzer("TopSingleLeptonDQM",
  ## ------------------------------------------------------
  ## SETUP
  ##
  ## configuration of the MonitoringEnsemble(s)
  ## [mandatory] : optional PSets may be omitted
  ##
  setup = cms.PSet(
    ## sub-directory to write the monitor histograms to
    ## [mandatory] : should not be changed w/o explicit
    ## communication to TopCom!
    directory = cms.string("Physics/Top/TopSingleElectronMediumDQM/"),
    ## [mandatory]
    sources = cms.PSet(
      muons = cms.InputTag("pfIsolatedMuonsEI"),
      elecs = cms.InputTag("pfIsolatedElectronsEI"),
      jets  = cms.InputTag("ak4PFJetsCHS"),
      mets  = cms.VInputTag("pfMet"),
      pvs   = cms.InputTag("offlinePrimaryVertices")

    ),
    ## [optional] : when omitted the verbosity level is set to STANDARD
    monitoring = cms.PSet(
      verbosity = cms.string("DEBUG")
    ),
    ## [optional] : when omitted all monitoring plots for primary vertices
    ## will be filled w/o extras
    pvExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the primary vertex candidates                                                                                            
      select   = cms.string(PVCut)
    ),
    ## [optional] : when omitted all monitoring plots for electrons
    ## will be filled w/o extras
    elecExtras = cms.PSet(
      ## when omitted electron plots will be filled w/o cut on electronId
      #electronId = cms.PSet( src = cms.InputTag("mvaTrigV0"), cutValue = cms.double(0.0) ),
      ## when omitted electron plots will be filled w/o additional pre-
      ## selection of the electron candidates
      select     = cms.string(looseEleCut + "& pt>20 & abs(eta)<2.5"),
			rho = cms.InputTag("fixedGridRhoFastjetAll"),
      ## when omitted isolated electron multiplicity plot will be equi-
      ## valent to inclusive electron multiplicity plot 
      ## isolation  = cms.string(ElelooseIsoCut),
    ),
    ## [optional] : when omitted all monitoring plots for jets
    ## will be filled w/o extras
    jetExtras = cms.PSet(
      ## when omitted monitor plots for pt will be filled from uncorrected
      ## jets
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      ## when omitted monitor plots will be filled w/o additional cut on
      ## jetID
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
   #   ),
      ## when omitted no extra selection will be applied on jets before
      ## filling the monitor histograms; if jetCorrector is present the
      ## selection will be applied to corrected jets 
      select = cms.string("pt>30 & abs(eta)<2.4 & " + looseJetCut),
      ## when omitted monitor histograms for b-tagging will not be filled
      jetBTaggers  = cms.PSet(
			cvsVertex = cms.PSet(
          label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
	          workingPoint = cms.double(0.970)
	          # CSV Tight from https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation74X
        )
      ),                                                
    ),
    ## [optional] : when omitted no mass window will be applied
    ## for the W mass before filling the event monitoring plots
    massExtras = cms.PSet(
      lowerEdge = cms.double( 70.),
      upperEdge = cms.double(110.)
    ),
    ## [optional] : when omitted the monitoring plots for triggering
    ## will be empty
    #triggerExtras = cms.PSet(
    #  src   = cms.InputTag("TriggerResults","","HLT"),
    #  paths = cms.vstring([ 'HLT_Ele15_LW_L1R:HLT_QuadJetU15'])
    #)
  ),
  ## ------------------------------------------------------
  ## PRESELECTION
  ##
  ## setup of the event preselection, which will not
  ## be monitored
  ## [mandatory] : but may be empty
  ##
  preselection = cms.PSet(
    ## [optional] : when omitted no preselection is applied
    #trigger = cms.PSet(
    #  src    = cms.InputTag("TriggerResults","","HLT"),
    #  select = cms.vstring(['HLT_Ele15_SW_CaloEleId_L1R'])
    #),
    ## [optional] : when omitted no preselection is applied
    vertex = cms.PSet(
      src    = cms.InputTag("offlinePrimaryVertices"),
      select = cms.string(PVCut)
    )
  ),
  ## ------------------------------------------------------
  ## SELECTION
  ##
  ## monitor histrograms are filled after each selection
  ## step, the selection is applied in the order defined
  ## by this vector
  ## [mandatory] : may be empty or contain an arbitrary
  ## number of PSets
  selection = cms.VPSet(
    cms.PSet(
      label = cms.string("elecs:step0"),
      src   = cms.InputTag("pfIsolatedElectronsEI"),
      select = cms.string("pt>30 & abs(eta)<2.5 & " + tightEleCut),
      min = cms.int32(1),
      max = cms.int32(1),
    ),
    cms.PSet(
      label = cms.string("jets/pf:step1"),
      src   = cms.InputTag("ak4PFJetsCHS"),
      jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30 & abs(eta)<2.4 & " + looseJetCut),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
#      ),
      min = cms.int32(4),
    ), 
    cms.PSet(
      label  = cms.string("met/pf:step2"),
      src    = cms.InputTag("pfMet"),
      #jetCorrector = cms.string("topDQMak5PFCHSL2L3"),
      select = cms.string("pt>30"),
      #jetID  = cms.PSet(
        #label  = cms.InputTag("ak5JetID"),
        #select = cms.string("fHPD < 0.98 & n90Hits>1 & restrictedEMF<1")
   		#),
      #min = cms.int32(4),
    ),
  )
)
