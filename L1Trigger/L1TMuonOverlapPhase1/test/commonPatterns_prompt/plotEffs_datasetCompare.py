import pickle
import math
import ROOT
import os
pileups = [0]#[0,140,200]#200]#,300]
modes   = ["AP_newEta","DP_newEta", "BOTH_newEta"]
color = [ROOT.kBlack, ROOT.kRed, ROOT.kBlue]
qualities = ['_q12']
types = ['Prompt_pt30']
outFile = ROOT.TFile("tdr_eff.root","RECREATE")
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
totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'].SetTitle(";Generated muon p_{T} [GeV];Efficiency")
totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'].SetLineColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'].SetMarkerColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['eff_pt0_q12_2GeV'].SetLineColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['eff_pt0_q12_2GeV'].SetMarkerColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['eff_pt0_q12_2GeV'].SetLineColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['eff_pt0_q12_2GeV'].SetMarkerColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'].Draw()
totalDict["Prompt_pt30_AP_newEta"]['eff_pt0_q12_2GeV'].Draw("same")
totalDict["Prompt_pt30_DP_newEta"]['eff_pt0_q12_2GeV'].Draw("same")
canvas.Update()
gr = totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["Prompt_pt30_BOTH_newEta"]['eff_pt0_q12_2GeV'],'All patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_AP_newEta"]['eff_pt0_q12_2GeV'],'Prompt patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_DP_newEta"]['eff_pt0_q12_2GeV'],'Displaced patterns','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_pt_eff_comparison.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_pt_eff_comparison.png')

canvas = ROOT.TCanvas("c","c", 800,600)# CreateCanvas('name2',False,True)
canvas.cd()
totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'].SetTitle(";Generated muon #eta ;Efficiency")
totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'].SetLineColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'].SetMarkerColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['hEta0_q12_cut0'].SetLineColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['hEta0_q12_cut0'].SetMarkerColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['hEta0_q12_cut0'].SetLineColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['hEta0_q12_cut0'].SetMarkerColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'].Draw()
totalDict["Prompt_pt30_AP_newEta"]['hEta0_q12_cut0'].Draw("same")
totalDict["Prompt_pt30_DP_newEta"]['hEta0_q12_cut0'].Draw("same")
canvas.Update()
gr = totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["Prompt_pt30_BOTH_newEta"]['hEta0_q12_cut0'],'All patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_AP_newEta"]['hEta0_q12_cut0'],'Prompt patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_DP_newEta"]['hEta0_q12_cut0'],'Displaced patterns','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_eta_eff_comparison.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_eta_eff_comparison.png')


canvas = ROOT.TCanvas("c","c", 800,600)# CreateCanvas('name2',False,True)
canvas.cd()
totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'].SetTitle(";Generated muon #eta ;Efficiency")
totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'].SetLineColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'].SetMarkerColor(totalDict["Prompt_pt30_BOTH_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['hDxy_q12_30steps'].SetLineColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_AP_newEta"]['hDxy_q12_30steps'].SetMarkerColor(totalDict["Prompt_pt30_AP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['hDxy_q12_30steps'].SetLineColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_DP_newEta"]['hDxy_q12_30steps'].SetMarkerColor(totalDict["Prompt_pt30_DP_newEta"]["color"])
totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'].Draw()
totalDict["Prompt_pt30_AP_newEta"]['hDxy_q12_30steps'].Draw("same")
totalDict["Prompt_pt30_DP_newEta"]['hDxy_q12_30steps'].Draw("same")
canvas.Update()
gr = totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'].GetPaintedGraph()
gr.SetMinimum(0.)
gr.SetMaximum(1.)
canvas.Update()
leg = ROOT.TLegend(0.5,0.65,0.9,0.9);
leg.SetTextSize(0.035);
leg.AddEntry(totalDict["Prompt_pt30_BOTH_newEta"]['hDxy_q12_30steps'],'All patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_AP_newEta"]['hDxy_q12_30steps'],'Prompt patterns','l');
leg.AddEntry(totalDict["Prompt_pt30_DP_newEta"]['hDxy_q12_30steps'],'Displaced patterns','l');
leg.Draw("same")
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_dxy_eff_comparison.pdf')
canvas.SaveAs('~/www/omtf_2020/Oct07/tdr_dxy_eff_comparison.png')

