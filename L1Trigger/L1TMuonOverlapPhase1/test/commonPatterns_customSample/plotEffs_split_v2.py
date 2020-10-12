import pickle
import math
import ROOT
import os
pileups = [0]#[0,140,200]#200]#,300]
modes   = ["BOTH_newEta_veto"]
color = [ROOT.kBlack, ROOT.kGreen+1, ROOT.kBlue]
qualities = ['_q12']
types = ['SplitDisp_pt30']
outFile = ROOT.TFile("tdrveto_eff.root","RECREATE")
outFile.cd()

ROOT.gROOT.SetBatch(True)
totalDict = {}

iColor = 0
for mode in modes:
  for typ in types:
      dataset = typ + "_" + mode
      with open('tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+  ".pickle"), 'rb') as handle:
          b = pickle.load(handle)
          print 'tdr_eff_SingleMu.pickle'.replace(".pickle",dataset + ".pickle")
      totalDict[dataset] = b[dataset]
      totalDict[dataset]["color"] = color[iColor]
      iColor += 1

#First, the plots on pT


canvas = ROOT.TCanvas("c","c", 800,600)# CreateCanvas('name2',False,True)
canvas.cd()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'].SetTitle(";Generated muon p_{T} [GeV];Efficiency")
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'].SetLineColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'].SetMarkerColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'].Draw()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeVp1000'].SetLineColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeVp1000'].SetMarkerColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeVp1000'].Draw("same")


canvas.Update()
gr = totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeV'],'All patterns','l');
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['eff_pt0_q12_2GeVp1000'],'Displaced patterns in all','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_pt_eff_comparisonStacked.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_pt_eff_comparisonStacked.png')

canvas = ROOT.TCanvas("c","c", 800,600)# CreateCanvas('name2',False,True)
canvas.cd()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'].SetTitle(";Generated muon #eta ; Efficiency")
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'].SetLineColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'].SetMarkerColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'].Draw()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0p1000'].SetLineColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0p1000'].SetMarkerColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0p1000'].Draw("same")


canvas.Update()
gr = totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0'],'All patterns','l');
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hEta0_q12_cut0p1000'],'Displaced patterns in all','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_eta_eff_comparisonStacked.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_eta_eff_comparisonStacked.png')


canvas = ROOT.TCanvas("c","c", 800,600)# CreateCanvas('name2',False,True)
canvas.cd()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'].SetTitle(";Generated muon d_{xy} ; Efficiency")
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'].SetLineColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'].SetMarkerColor(ROOT.kBlack)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'].Draw()
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30stepsp1000'].SetLineColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30stepsp1000'].SetMarkerColor(ROOT.kGreen+1)
totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30stepsp1000'].Draw("same")


canvas.Update()
gr = totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30steps'],'All patterns','l');
leg.AddEntry(totalDict["SplitDisp_pt30_BOTH_newEta_veto"]['hDxy_q12_30stepsp1000'],'Displaced patterns in all','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_dxy_eff_comparisonStacked.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct06/tdrveto_dxy_eff_comparisonStacked.png')

