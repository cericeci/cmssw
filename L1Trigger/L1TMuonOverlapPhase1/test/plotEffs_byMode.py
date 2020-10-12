import pickle
import math
import ROOT
import os

ROOT.gROOT.SetBatch(True)
tags = ["dxy0", "dxy10", "dxy20", "dxy30"] 
colors = {"dxy0":ROOT.kRed,"dxy10":ROOT.kGreen,"dxy20":ROOT.kBlue,"dxy30":ROOT.kBlack}
pretty = {"dxy0":"|d_{xy}| < 0.1", "dxy10":"0.1 <|d_{xy}| < 0.2","dxy20":"0.2 < |d_{xy}| < 0.3","dxy30":"0.3 < |d_{xy}|"}
picks = {}
canvas = ROOT.TCanvas("c1","c1",800,600) #CreateCanvas('name',False,True)


with open("tdr_eff_SingleMuDisp_HighPt_PU200_DP_all.pickle", 'rb') as handle:
  picks["Disp"] = pickle.load(handle)["Disp_HighPt_PU200_DP_all"]

with open("tdr_eff_SingleMuDisp_HighPt_PU200_SP.pickle", 'rb') as handle:
  picks["Prompt"] = pickle.load(handle)["Disp_HighPt_PU200_SP"]

with open("tdr_eff_SingleMuDisp_HighPt_PU200_AP.pickle", 'rb') as handle:
  picks["All"] = pickle.load(handle)["Disp_HighPt_PU200_AP"]



canvas9 = ROOT.TCanvas("c4","c4",800,600) #CreateCanvas('name8',False,True)
canvas9.cd()

leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
leg.SetTextSize(0.025);
#leg.AddEntry(picks["all"]["Disp_HighPt_PU200_DP_all"]['hDxy_q12_30steps'],"l","All")
print picks["Prompt"]
picks["Disp"]['hDxy_q12_30steps'].SetLineColor(ROOT.kRed)
picks["Disp"]['hDxy_q12_30steps'].SetTitle(";Generated muon  d_{xy};Efficiency")
leg.AddEntry(picks["Disp"]['hDxy_q12_30steps'],"Displaced","l")
picks["Disp"]['hDxy_q12_30steps'].Draw()
canvas9.Update()
picks["Disp"]['hDxy_q12_30steps'].GetPaintedGraph().SetMaximum(0.2)
picks["Prompt"]['hDxy_q12_30steps'].SetLineColor(ROOT.kBlue)
leg.AddEntry(picks["Prompt"]['hDxy_q12_30steps'],"Prompt","l")
picks["Prompt"]['hDxy_q12_30steps'].Draw(" same")

picks["All"]['hDxy_q12_30steps'].SetLineColor(ROOT.kBlack)
leg.AddEntry(picks["All"]['hDxy_q12_30steps'],"Prompt or Displaced","l")
picks["All"]['hDxy_q12_30steps'].Draw(" same")

leg.Draw("same")
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_dxy_modesplit_DispHighPt.pdf')
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_dxy_modesplit_DispHighPt.png')
