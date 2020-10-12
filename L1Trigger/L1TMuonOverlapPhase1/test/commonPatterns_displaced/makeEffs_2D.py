import os, re, ROOT, sys, pickle, time
from pprint import pprint
from math import *
from array import array
from DataFormats.FWLite import Events, Handle
import numpy as np

datasets = {
   #'SingleMu_NOPU_AP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/SingleMu_NOPU/200724_205105/0000/',},
   #'SingleMu_PU200_AP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/SingleMu_PU200/200724_205713/0000/',},
   #'SingleMu_PU300_AP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/SingleMu_PU300/200724_205542/0000/',},  #1 2 
    #'SingleMu_NOPU_SP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/SingleMu_NOPU/200724_205105/0000/',},
    #'SingleMu_PU200_SP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/SingleMu_PU200/200723_205609/0000/',},
    #'SingleMu_PU300_SP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/SingleMu_PU300/200723_205440/0000/',},

   #'Disp_LowPt_NoPU_AP'   : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/Disp_2to10_0to3000_NoPU/200724_204327/0000/',},
   #'Disp_LowPt_PU200_AP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/Disp_2to10_0to3000_PU200/200724_205409/0000/',},
    #'Disp_MidPt_NoPU_SP'   : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/Disp_10to30_0to3000_NoPU/200723_204657/0000/',},
    #'Disp_MidPt_PU200_SP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/Disp_10to30_0to3000_PU200/200723_204524/0000/',},
    #'Disp_HighPt_NoPU_SP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/D',},
    #'Disp_HighPt_PU200_SP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/Disp_30to100_0to3000_PU200/200723_205133/0000/',},

    #'Disp_LowPt_NoPU_SP'   : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/Disp_2to10_0to3000_NoPU/200723_204216/0000/',},
    #'Disp_LowPt_PU200_SP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/Disp_2to10_0to3000_PU200/200723_205307/0000/',},
   #'Disp_MidPt_NoPU_AP'   : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/Disp_10to30_0to3000_NoPU/200724_204759/0000/',},
   #'Disp_MidPt_PU200_AP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/Disp_10to30_0to3000_PU200/200724_204628/0000/',},
    #'Disp_HighPt_NoPU_SP'  : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/24Jul_bothPatterns/',},
   #'Disp_HighPt_PU200_AP' : { 'path' : '/pool/phedex/userstorage/carlosec/omtf/results/27Jul_bothPatterns/Disp_30to100_0to3000_PU200/200724_205234/0000/',},
    #'SingleMu_NOPU_aging1000'  : { 'path' : '/eos/cms/store/group/phys_muon/cericeci/overlap_oct22/Mu_FlatPt2to100-pythia8-gun/SingleMu_NOPU/191031_163317/0000/',},
    #'SingleMu_PU200_aging1000' : { 'path' : '/eos/cms/store/group/phys_muon/cericeci/overlap_oct22/Mu_FlatPt2to100-pythia8-gun/SingleMu_PU200/191031_155204/0000/',},
    #'SingleMu_NOPU_aging3000'  : { 'path' : '/eos/cms/store/group/phys_muon/cericeci/overlap_oct22/Mu_FlatPt2to100-pythia8-gun/SingleMu_NOPU/191031_155658/0000/',},
    #'SingleMu_PU200_aging3000' : { 'path' : '/eos/cms/store/group/phys_muon/cericeci/overlap_oct22/Mu_FlatPt2to100-pythia8-gun/SingleMu_PU200/191031_155834/0000/',},
   #'Disp_HighPt_PU200_DP_modeta' : { 'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/newEtaDisp/',},
   #'SingleMu_PU200_DP_modeta' : { 'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/newEtaPrompt/'},
   #'Disp_HighPt_PU200_AP_modeta' : { 'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/newEtaDisp/',},
   #'SingleMu_PU200_AP_modeta' : { 'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/newEtaPrompt/'},
   'Disp_pt30_DOUBLE' : {'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/commonPatterns/'}, 
   'Disp_pt30_DOUBLE_newEta' : {'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/commonPatterns/'},
}

pickleName = 'tdr_eff_SingleMu.pickle'

def getEta(etaHW):
    return  etaHW/240.*2.61

def getPt(ptHW):
    return max((ptHW-1.)/2., 1)

def modulo(val):
    while val > 2*pi: val -= 2*pi
    while val <0: val += 2*pi
    return val

def getPhi(obj):
    return modulo(((15.+obj.processor()*60.)/360. + obj.hwPhi()/576.)*2*pi)

def getP4(obj):
    pt = obj.pt()
    eta= obj.eta()
    phi= obj.phi()
    v = ROOT.TLorentzVector()
    v.SetPtEtaPhiM( pt, eta, phi, 0)
    return v

def getP4FromHW(obj):
    pt = obj.hwPt()
    eta= obj.hwEta()
    phi= obj.hwPhi()
    v = ROOT.TLorentzVector()
    v.SetPtEtaPhiM( getPt(pt), getEta(eta), getPhi(obj), 0)
    return v






for dataset in datasets:
    thefiles = []
    fileList = []
    print dataset
    if type(datasets[dataset]['path']) == type([1,2]): 
        for item in datasets[dataset]['path']:
            fileList = fileList + [item + "/" + f for f in os.listdir(item)]
    else:
        fileList = [datasets[dataset]['path'] + "/" + f for f in os.listdir(datasets[dataset]['path'])]
    
    for files in fileList:
        #fil = filter( lambda x : '.root' in x and "super" in x, files)
        if not(".root" in files and "super" in files): continue
        thefiles.append(files)
    datasets[dataset]['files'] = thefiles

commonHandle, commonLabel=  Handle("BXVector<l1t::RegionalMuonCand>"), ("simBayesOmtfDigisBoth", "OMTF", "L1TMuonEmulation" )
dispHandle, dispLabel = Handle("BXVector<l1t::RegionalMuonCand>"), ("simBayesOmtfDigisDisplaced", "OMTF", "L1TMuonEmulation" )
muonHandle, muonLabel = Handle("BXVector<l1t::RegionalMuonCand>"), ("simBayesOmtfDigis", "OMTF", "L1TMuonEmulation" )
genHandle, genLabel = Handle("vector<reco::GenParticle>"), "genParticles"
newEtaHandle, newEtaLabel = Handle("edm::ValueMap<float>"), ( "dispGenEta","genParticledispEta","MuonMatcher") 
newPhiHandle, newPhiLabel = Handle("edm::ValueMap<float>"), ( "dispGenEta","genParticledispPhi","MuonMatcher")

maxEvents = -1

for dataset in datasets:
    outputDict = {}
    print 'starting to process', dataset
    events = Events(datasets[dataset]['files'])
    print 'we got the events'

    ptBins = array('f',[0.,1.,2.,3.,4.,4.5,5.,6.,7.,8.,10.,12.,14.,16.,18.,20.,25.,30.,35.,40.,45.,50.,60.,70.,80.,90.,100.,120.,140.,200.])
    dxyBins = array('f',[0.,0.1,0.2,0.3,0.4])
    hPt_dXY = ROOT.TH2D('h2D','h2D', len(ptBins)-1, ptBins, len(dxyBins)-1, dxyBins)
    outputDict[dataset] = { }
    outputDict[dataset]['hPt_dXY'] = hPt_dXY


    print 'here :)'
    count = 0
    for ev in events:
        #print "Event!"
        if not count%1000:  print count, events.size()
        count = count + 1
        #if count == 1000: break
        if count > maxEvents and maxEvents > 0: break
        ev.getByLabel(commonLabel, commonHandle)
        ev.getByLabel(dispLabel, dispHandle)
        ev.getByLabel(muonLabel, muonHandle)
        ev.getByLabel(genLabel, genHandle)
        ev.getByLabel(newEtaLabel, newEtaHandle)
        ev.getByLabel(newPhiLabel, newPhiHandle)
        muons = muonHandle.product()
        dispmuons = dispHandle.product()
        allmuons  = commonHandle.product()
        gens  = genHandle.product()
        newEta= newEtaHandle.product()
        newPhi= newPhiHandle.product()
        #print newEta.get(0), newPhi.get(0)
        goodmuons = []
        types = []
        goodIndex = 0
        for bxNumber in range(muons.getFirstBX(), muons.getLastBX()+1):
           
            size = muons.size(bxNumber)
            for i in range(size):
                muon = muons[i+goodIndex]
                #if muon.trackFinderType() not in [1,2]: continue
                #if muon.hwQual() < 12: continue

                goodmuons.append( muon)
                #print "RECO:", getP4FromHW(muon).Pt()
                types.append("Prompt")
            goodIndex = goodIndex + size
        #print "Next event!"

        goodIndex = 0
        for bxNumber in range(dispmuons.getFirstBX(), dispmuons.getLastBX()+1):

            size = dispmuons.size(bxNumber)
            for i in range(size):
                muon = dispmuons[i+goodIndex]
                #if muon.trackFinderType() not in [1,2]: continue
                #if muon.hwQual() < 12: continue

                goodmuons.append( muon)
                #print "RECO:", getP4FromHW(muon).Pt()
                types.append("Displaced")
            goodIndex = goodIndex + size



        ig = 0
        for gen in gens:
            if abs(gen.pdgId()) != 13: continue
            # Now update the thingies
            if "newEta" in dataset:
              newp4 = ROOT.Math.LorentzVector("ROOT::Math::PtEtaPhiM4D<double>")(gen.pt(), newEta.get(ig), newPhi.get(ig), gen.mass())
              gen.setP4(newp4)
            ig += 1

            rematchedPt = 0
            foundPrompt = False
            foundDisplaced = False
            for i,mu in enumerate(goodmuons):
                v_mu = getP4FromHW(mu)
                #if toprint: print "L1 Cand: ", v_mu.Pt(), v_mu.Eta(), v_mu.Phi(), muon.hwQual()
                v_gen = getP4(gen) 
                if v_mu.DeltaR( v_gen ) < 0.5 and mu.hwQual() >= 12:
                   if types[i] == "Prompt": foundPrompt = v_mu.Pt()
                   if types[i] == "Displaced":
                     if v_mu.Pt() < 0.1 : foundDisplaced = 0.05
                     elif v_mu.Pt() < 6000 : foundDisplaced = 0.15
                     elif v_mu.Pt() < 11000 : foundDisplaced = 0.25
                     else : foundDisplaced = 0.35

            if foundDisplaced and foundPrompt:
               hPt_dXY.Fill(foundPrompt, foundDisplaced)

    import pickle
    with open(pickleName.replace(".pickle",dataset+".pickle"), 'wb') as handle:
       pickle.dump(outputDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    canvas= ROOT.TCanvas("c","c",800,600)
    hPt_dXY.Draw("textcolz")
    canvas.SaveAs("test"+ dataset +".pdf")

