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
  picks["all"] = pickle.load(handle)

for t in tags:
 with open("tdr_eff_SingleMuDisp_HighPt_PU200_DP_%s.pickle"%t, 'rb') as handle:
  picks[t] = pickle.load(handle)


canvas9 = ROOT.TCanvas("c4","c4",800,600) #CreateCanvas('name8',False,True)
canvas9.cd()

leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
leg.SetTextSize(0.025);
#leg.AddEntry(picks["all"]["Disp_HighPt_PU200_DP_all"]['hDxy_q12_30steps'],"l","All")

first = True
toPlot = {}
for t in tags:
  if first:
    first = False
    thePass = picks[t]["Disp_HighPt_PU200_DP_%s"%t]['hDxy_q12_30steps'].GetPassedHistogram() 
    theTotal= picks[t]["Disp_HighPt_PU200_DP_%s"%t]['hDxy_q12_30steps'].GetTotalHistogram()
    toPlot[t] = ROOT.TEfficiency(thePass,theTotal)
    toPlot[t].SetLineColor(colors[t])
    toPlot[t].SetTitle(";Generated muon  d_{xy};Efficiency")
    leg.AddEntry(toPlot[t],pretty[t],"l")
    toPlot[t].Draw()
    canvas9.Update()
    toPlot[t].GetPaintedGraph().SetMaximum(0.2)
  else:
    theAddPass = picks[t]["Disp_HighPt_PU200_DP_%s"%t]['hDxy_q12_30steps'].GetPassedHistogram()
    thePass = thePass + theAddPass
    toPlot[t] = ROOT.TEfficiency(thePass,theTotal)
    toPlot[t].SetLineColor(colors[t])
    leg.AddEntry(toPlot[t]," + " + pretty[t],"l")

  toPlot[t].Draw(" same")


leg.Draw("same")
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_dxy_patternsplit_DispHighPt.pdf')
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_dxy_patternsplit_DispHighPt.png')
