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
   #'SplitPrompt_pt30_BOTH_veto' : {'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/commonPatterns_displaced/'},
   'SplitPrompt_pt30_BOTH_newEta_veto' : {'path' : '/nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/commonPatterns_prompt/'},
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
    hEta20_q12_cut20   = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta5_20_q12_cut20  = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta5_20_q12_cut0   = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta10_q12_cut5     = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta5_q12_cut5      = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta0_q12_cut0      = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta7_10_q12_cut5   = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta7_15_q12_cut5   = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hEta7_20_q12_cut5   = ROOT.TEfficiency("hEta20_%s_q12"%dataset,"",240,-2.4,2.4)
    hPt0_q12_5GeV     = ROOT.TEfficiency("hPt0_%s_q12_5"%dataset,"",20,0,100)
    hPt3_q12_5GeV     = ROOT.TEfficiency("hPt3_%s_q12_5"%dataset,"",20,0,100)
    hPt10_q12_5GeV    = ROOT.TEfficiency("hPt10_%s_q12_5"%dataset,"",20,0,100)
    hPt20_q12_5GeV    = ROOT.TEfficiency("hPt20_%s_q12_5"%dataset,"",20,0,100)
    hPt0_q12_3GeV     = ROOT.TEfficiency("hPt0_%s_q12_3"%dataset,"",34,0,102)
    hPt3_q12_3GeV     = ROOT.TEfficiency("hPt3_%s_q12_3"%dataset,"",34,0,102)
    hPt10_q12_3GeV    = ROOT.TEfficiency("hPt10_%s_q12_3"%dataset,"",34,0,102)
    hPt20_q12_3GeV    = ROOT.TEfficiency("hPt20_%s_q12_3"%dataset,"",34,0,102)
    hPt0_q12_2GeV     = ROOT.TEfficiency("hPt0_%s_q12_2"%dataset,"",50,0,100)
    hPt3_q12_2GeV     = ROOT.TEfficiency("hPt3_%s_q12_2"%dataset,"",50,0,100)
    hPt10_q12_2GeV    = ROOT.TEfficiency("hPt10_%s_q12_2"%dataset,"",50,0,100)
    hPt20_q12_2GeV    = ROOT.TEfficiency("hPt20_%s_q12_2"%dataset,"",50,0,100)
    hPt0_q12_1GeV     = ROOT.TEfficiency("hPt0_%s_q12_1"%dataset,"",100,0,100)
    hPt3_q12_1GeV     = ROOT.TEfficiency("hPt3_%s_q12_1"%dataset,"",100,0,100)
    hPt10_q12_1GeV    = ROOT.TEfficiency("hPt10_%s_q12_1"%dataset,"",100,0,100)
    hPt20_q12_1GeV    = ROOT.TEfficiency("hPt20_%s_q12_1"%dataset,"",100,0,100)
    hDxy_q12_10steps  = ROOT.TEfficiency("hDxy_%s_q12_10steps"%dataset,"",10,0,300)
    hDxy_q12_30steps  = ROOT.TEfficiency("hDxy_%s_q12_30steps"%dataset,"",30,0,300)
    hDxy_q12_100steps  = ROOT.TEfficiency("hDxy_%s_q12_100steps"%dataset,"",100,0,300)
    outputDict[dataset] = { }
    outputDict[dataset]['hEta20_q12_cut20']   = hEta20_q12_cut20
    outputDict[dataset]['hEta5_20_q12_cut20'] = hEta5_20_q12_cut20
    outputDict[dataset]['hEta5_20_q12_cut0']  = hEta5_20_q12_cut0
    outputDict[dataset]['hEta10_q12_cut5']    = hEta10_q12_cut5
    outputDict[dataset]['hEta5_q12_cut5']     = hEta5_q12_cut5
    outputDict[dataset]['hEta0_q12_cut0']     = hEta0_q12_cut0
    outputDict[dataset]['hEta7_10_q12_cut5']    = hEta7_10_q12_cut5
    outputDict[dataset]['hEta7_15_q12_cut5']    = hEta7_15_q12_cut5
    outputDict[dataset]['hEta7_20_q12_cut5']    = hEta7_20_q12_cut5
    outputDict[dataset]['eff_pt0_q12_5GeV']     = hPt0_q12_5GeV
    outputDict[dataset]['eff_pt3_q12_5GeV']     = hPt3_q12_5GeV
    outputDict[dataset]['eff_pt10_q12_5GeV']    = hPt10_q12_5GeV
    outputDict[dataset]['eff_pt20_q12_5GeV']    = hPt20_q12_5GeV
    outputDict[dataset]['eff_pt0_q12_3GeV']     = hPt0_q12_3GeV
    outputDict[dataset]['eff_pt3_q12_3GeV']     = hPt3_q12_3GeV
    outputDict[dataset]['eff_pt10_q12_3GeV']    = hPt10_q12_3GeV
    outputDict[dataset]['eff_pt20_q12_3GeV']    = hPt20_q12_3GeV
    outputDict[dataset]['eff_pt0_q12_2GeV']     = hPt0_q12_2GeV
    outputDict[dataset]['eff_pt3_q12_2GeV']     = hPt3_q12_2GeV
    outputDict[dataset]['eff_pt10_q12_2GeV']    = hPt10_q12_2GeV
    outputDict[dataset]['eff_pt20_q12_2GeV']    = hPt20_q12_2GeV
    outputDict[dataset]['eff_pt0_q12_1GeV']     = hPt0_q12_1GeV
    outputDict[dataset]['eff_pt3_q12_1GeV']     = hPt3_q12_1GeV
    outputDict[dataset]['eff_pt10_q12_1GeV']    = hPt10_q12_1GeV
    outputDict[dataset]['eff_pt20_q12_1GeV']    = hPt20_q12_1GeV
    outputDict[dataset]['hDxy_q12_10steps']     = hDxy_q12_10steps
    outputDict[dataset]['hDxy_q12_30steps']     = hDxy_q12_30steps
    outputDict[dataset]['hDxy_q12_100steps']     = hDxy_q12_100steps

    hEta20_q12_cut20p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta5_20_q12_cut20p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta5_20_q12_cut0p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta10_q12_cut5p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta5_q12_cut5p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta0_q12_cut0p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta7_10_q12_cut5p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta7_15_q12_cut5p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hEta7_20_q12_cut5p1000 = ROOT.TEfficiency("hEta20_%s_q12"%dataset+"p1000","",240,-2.4,2.4)
    hPt0_q12_5GeVp1000 = ROOT.TEfficiency("hPt0_%s_q12_5"%dataset+"p1000","",20,0,100)
    hPt3_q12_5GeVp1000 = ROOT.TEfficiency("hPt3_%s_q12_5"%dataset+"p1000","",20,0,100)
    hPt10_q12_5GeVp1000 = ROOT.TEfficiency("hPt10_%s_q12_5"%dataset+"p1000","",20,0,100)
    hPt20_q12_5GeVp1000 = ROOT.TEfficiency("hPt20_%s_q12_5"%dataset+"p1000","",20,0,100)
    hPt0_q12_3GeVp1000 = ROOT.TEfficiency("hPt0_%s_q12_3"%dataset+"p1000","",34,0,102)
    hPt3_q12_3GeVp1000 = ROOT.TEfficiency("hPt3_%s_q12_3"%dataset+"p1000","",34,0,102)
    hPt10_q12_3GeVp1000 = ROOT.TEfficiency("hPt10_%s_q12_3"%dataset+"p1000","",34,0,102)
    hPt20_q12_3GeVp1000 = ROOT.TEfficiency("hPt20_%s_q12_3"%dataset+"p1000","",34,0,102)
    hPt0_q12_2GeVp1000 = ROOT.TEfficiency("hPt0_%s_q12_2"%dataset+"p1000","",50,0,100)
    hPt3_q12_2GeVp1000 = ROOT.TEfficiency("hPt3_%s_q12_2"%dataset+"p1000","",50,0,100)
    hPt10_q12_2GeVp1000 = ROOT.TEfficiency("hPt10_%s_q12_2"%dataset+"p1000","",50,0,100)
    hPt20_q12_2GeVp1000 = ROOT.TEfficiency("hPt20_%s_q12_2"%dataset+"p1000","",50,0,100)
    hPt0_q12_1GeVp1000 = ROOT.TEfficiency("hPt0_%s_q12_1"%dataset+"p1000","",100,0,100)
    hPt3_q12_1GeVp1000 = ROOT.TEfficiency("hPt3_%s_q12_1"%dataset+"p1000","",100,0,100)
    hPt10_q12_1GeVp1000 = ROOT.TEfficiency("hPt10_%s_q12_1"%dataset+"p1000","",100,0,100)
    hPt20_q12_1GeVp1000 = ROOT.TEfficiency("hPt20_%s_q12_1"%dataset+"p1000","",100,0,100)
    hDxy_q12_10stepsp1000 = ROOT.TEfficiency("hDxy_%s_q12_10steps"%dataset+"p1000","",10,0,300)
    hDxy_q12_30stepsp1000 = ROOT.TEfficiency("hDxy_%s_q12_30steps"%dataset+"p1000","",30,0,300)
    hDxy_q12_100stepsp1000 = ROOT.TEfficiency("hDxy_%s_q12_100steps"%dataset+"p1000","",100,0,300)

    outputDict[dataset]['hEta20_q12_cut20p1000']   = hEta20_q12_cut20p1000
    outputDict[dataset]['hEta5_20_q12_cut20p1000'] = hEta5_20_q12_cut20p1000
    outputDict[dataset]['hEta5_20_q12_cut0p1000']  = hEta5_20_q12_cut0p1000
    outputDict[dataset]['hEta10_q12_cut5p1000']    = hEta10_q12_cut5p1000
    outputDict[dataset]['hEta5_q12_cut5p1000']     = hEta5_q12_cut5p1000
    outputDict[dataset]['hEta0_q12_cut0p1000']     = hEta0_q12_cut0p1000
    outputDict[dataset]['hEta7_10_q12_cut5p1000']    = hEta7_10_q12_cut5p1000
    outputDict[dataset]['hEta7_15_q12_cut5p1000']    = hEta7_15_q12_cut5p1000
    outputDict[dataset]['hEta7_20_q12_cut5p1000']    = hEta7_20_q12_cut5p1000
    outputDict[dataset]['eff_pt0_q12_5GeVp1000']     = hPt0_q12_5GeVp1000
    outputDict[dataset]['eff_pt3_q12_5GeVp1000']     = hPt3_q12_5GeVp1000
    outputDict[dataset]['eff_pt10_q12_5GeVp1000']    = hPt10_q12_5GeVp1000
    outputDict[dataset]['eff_pt20_q12_5GeVp1000']    = hPt20_q12_5GeVp1000
    outputDict[dataset]['eff_pt0_q12_3GeVp1000']     = hPt0_q12_3GeVp1000
    outputDict[dataset]['eff_pt3_q12_3GeVp1000']     = hPt3_q12_3GeVp1000
    outputDict[dataset]['eff_pt10_q12_3GeVp1000']    = hPt10_q12_3GeVp1000
    outputDict[dataset]['eff_pt20_q12_3GeVp1000']    = hPt20_q12_3GeVp1000
    outputDict[dataset]['eff_pt0_q12_2GeVp1000']     = hPt0_q12_2GeVp1000
    outputDict[dataset]['eff_pt3_q12_2GeVp1000']     = hPt3_q12_2GeVp1000
    outputDict[dataset]['eff_pt10_q12_2GeVp1000']    = hPt10_q12_2GeVp1000
    outputDict[dataset]['eff_pt20_q12_2GeVp1000']    = hPt20_q12_2GeVp1000
    outputDict[dataset]['eff_pt0_q12_1GeVp1000']     = hPt0_q12_1GeVp1000
    outputDict[dataset]['eff_pt3_q12_1GeVp1000']     = hPt3_q12_1GeVp1000
    outputDict[dataset]['eff_pt10_q12_1GeVp1000']    = hPt10_q12_1GeVp1000
    outputDict[dataset]['eff_pt20_q12_1GeVp1000']    = hPt20_q12_1GeVp1000
    outputDict[dataset]['hDxy_q12_10stepsp1000']     = hDxy_q12_10stepsp1000
    outputDict[dataset]['hDxy_q12_30stepsp1000']     = hDxy_q12_30stepsp1000
    outputDict[dataset]['hDxy_q12_100stepsp1000']     = hDxy_q12_100stepsp1000
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
        vetomuons = []
        goodIndex = 0

        if "BOTH" in dataset:
          for bxNumber in range(allmuons.getFirstBX(), allmuons.getLastBX()+1):

            size = allmuons.size(bxNumber)
            for i in range(size):
                muon = allmuons[i+goodIndex]
                #if muon.trackFinderType() not in [1,2]: continue
                #if muon.hwQual() < 12: continue

                goodmuons.append( muon)
                #print "RECO:", getP4FromHW(muon).Pt()

            goodIndex = goodIndex + size

        goodIndex = 0
        if "BOTH" in dataset:
          for bxNumber in range(muons.getFirstBX(), muons.getLastBX()+1):

            size = muons.size(bxNumber)
            for i in range(size):
                muon = muons[i+goodIndex]
                #if muon.trackFinderType() not in [1,2]: continue
                #if muon.hwQual() < 12: continue

                vetomuons.append( muon)
                #print "RECO:", getP4FromHW(muon).Pt()

            goodIndex = goodIndex + size



        ig = 0
        for gen in gens:
            if abs(gen.pdgId()) != 13: continue
            # Now update the thingies
            if "newEta" in dataset:
              newp4 = ROOT.Math.LorentzVector("ROOT::Math::PtEtaPhiM4D<double>")(gen.pt(), newEta.get(ig), newPhi.get(ig), gen.mass())
              gen.setP4(newp4)
            ig += 1
            #if abs(gen.eta()) >= 0.82 and abs(gen.eta()) <= 1.24: print " <=========================================="
            passes_0_12   = False
            passes_3_12  = False
            passes_5_12  = False
            passes_10_12 = False
            passes_20_12 = False
            v_gen = getP4(gen)
            dxy_gen = abs((-1*gen.vx()* v_gen.Py() + gen.vy()* v_gen.Px()) / v_gen.Pt())

            #if toprint: print "GEN: ", v_gen.Pt(), v_gen.Eta(), v_gen.Phi()
            rematchedPt = 0
            pt = 0
            for mu in goodmuons:
                v_mu = getP4FromHW(mu)
                #if toprint: print "L1 Cand: ", v_mu.Pt(), v_mu.Eta(), v_mu.Phi(), muon.hwQual()
                
                if v_mu.DeltaR( v_gen ) < 0.5 and mu.hwQual() >= 12:
                    pt = v_mu.Pt() + (1000* v_mu.Pt() < 0.1) # Just to make thinks clear when mixing displaced and non displaced
                    if pt >= 20: passes_20_12 = True
                    if pt >= 10: passes_10_12 = True
                    if pt >= 5 : passes_5_12  = True
                    if pt >= 3 : passes_3_12  = True
                    rematchedPt = v_mu.Pt()
                    passes_0_12 = True
                    if passes_20_12: break
            isVeto = False
            for mu in vetomuons:

                v_muveto = getP4FromHW(mu)
                #if toprint: print "L1 Cand: ", v_mu.Pt(), v_mu.Eta(), v_mu.Phi(), muon.hwQual()
                if v_muveto.DeltaR( v_gen ) < 0.5 and mu.hwQual() >= 12 and v_muveto.Pt() <= 10: isVeto=True


            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_5GeV.Fill( passes_0_12, v_gen.Pt())                 
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_5GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_5GeV.Fill( passes_10_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_5GeV.Fill( passes_20_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_3GeV.Fill( passes_0_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_3GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_3GeV.Fill( passes_10_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_3GeV.Fill( passes_20_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_2GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_2GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_2GeV.Fill( passes_10_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_2GeV.Fill( passes_20_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_1GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_1GeV.Fill( passes_3_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_1GeV.Fill( passes_10_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_1GeV.Fill( passes_20_12, v_gen.Pt())
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_10steps.Fill( passes_0_12, dxy_gen)
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_30steps.Fill( passes_0_12, dxy_gen)
            if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_100steps.Fill( passes_0_12, dxy_gen)


            #print passes_5_0, v_gen.Pt()
            #Now to the fun part with the eta
            if (v_gen.Pt() > 25):
                hEta20_q12_cut20.Fill(passes_20_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 5 and v_gen.Pt() < 20):
                hEta5_20_q12_cut20.Fill(passes_20_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 5 and v_gen.Pt() < 20):
                hEta5_20_q12_cut0.Fill(passes_0_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 10):
                hEta10_q12_cut5.Fill(passes_5_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 5):
                hEta5_q12_cut5.Fill(passes_5_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 7 and v_gen.Pt() < 10):
                hEta7_10_q12_cut5.Fill(passes_5_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 7 and v_gen.Pt() < 15):
                hEta7_15_q12_cut5.Fill(passes_5_12, abs(v_gen.Eta()))

            if (v_gen.Pt() > 7 and v_gen.Pt() < 20):
                hEta7_20_q12_cut5.Fill(passes_5_12, abs(v_gen.Eta()))
            hEta0_q12_cut0.Fill(passes_0_12, abs(v_gen.Eta()))

            passes_0_12 = pt >= 1000 and passes_0_12 and not(isVeto)
            passes_3_12 = pt >= 1000 and passes_3_12 and not(isVeto)
            passes_10_12 = pt >= 1000 and passes_10_12 and not(isVeto)
            passes_20_12 = pt >= 1000 and passes_20_12 and not(isVeto)
            if True:
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_5GeVp1000.Fill( passes_0_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_5GeVp1000.Fill( passes_3_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_5GeVp1000.Fill( passes_10_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_5GeVp1000.Fill( passes_20_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_3GeVp1000.Fill( passes_0_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_3GeVp1000.Fill( passes_3_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_3GeVp1000.Fill( passes_10_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_3GeVp1000.Fill( passes_20_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_2GeVp1000.Fill( passes_0_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_2GeVp1000.Fill( passes_3_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_2GeVp1000.Fill( passes_10_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_2GeVp1000.Fill( passes_20_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt0_q12_1GeVp1000.Fill( passes_0_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt3_q12_1GeVp1000.Fill( passes_3_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt10_q12_1GeVp1000.Fill( passes_10_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hPt20_q12_1GeVp1000.Fill( passes_20_12, v_gen.Pt())
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_10stepsp1000.Fill( passes_0_12, dxy_gen)
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_30stepsp1000.Fill( passes_0_12, dxy_gen)
             if abs(gen.eta()) < 1.24 and abs(gen.eta()) > 0.82: hDxy_q12_100stepsp1000.Fill( passes_0_12, dxy_gen)


             #print passes_5_0, v_gen.Pt()
             #Now to the fun part with the eta
             if (v_gen.Pt() > 25):
                 hEta20_q12_cut20p1000.Fill(passes_20_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 5 and v_gen.Pt() < 20):
                 hEta5_20_q12_cut20p1000.Fill(passes_20_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 5 and v_gen.Pt() < 20):
                 hEta5_20_q12_cut0p1000.Fill(passes_0_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 10):
                 hEta10_q12_cut5p1000.Fill(passes_5_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 5):
                 hEta5_q12_cut5p1000.Fill(passes_5_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 7 and v_gen.Pt() < 10):
                 hEta7_10_q12_cut5p1000.Fill(passes_5_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 7 and v_gen.Pt() < 15):
                hEta7_15_q12_cut5p1000.Fill(passes_5_12, abs(v_gen.Eta()))

             if (v_gen.Pt() > 7 and v_gen.Pt() < 20):
                hEta7_20_q12_cut5p1000.Fill(passes_5_12, abs(v_gen.Eta()))
             hEta0_q12_cut0p1000.Fill(passes_0_12, abs(v_gen.Eta()))



    import pickle
    with open(pickleName.replace(".pickle",dataset+".pickle"), 'wb') as handle:
       pickle.dump(outputDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
