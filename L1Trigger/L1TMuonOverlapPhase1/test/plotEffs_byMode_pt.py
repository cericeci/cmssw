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


with open("tdr_eff_SingleMuSingleMu_PU200_DP_all.pickle", 'rb') as handle:
  picks["all"] = pickle.load(handle)

for t in tags:
 with open("tdr_eff_SingleMuSingleMu_PU200_DP_%s.pickle"%t, 'rb') as handle:
  picks[t] = pickle.load(handle)


canvas9 = ROOT.TCanvas("c4","c4",800,600) #CreateCanvas('name8',False,True)
canvas9.cd()

leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
leg.SetTextSize(0.025);
#leg.AddEntry(picks["all"]["SingleMu_PU200_DP_all"]['eff_pt20_q12_3GeV'],"l","All")

first = True
toPlot = {}
for t in tags:
  if first:
    first = False
    thePass = picks[t]["SingleMu_PU200_DP_%s"%t]['eff_pt20_q12_3GeV'].GetPassedHistogram() 
    theTotal= picks[t]["SingleMu_PU200_DP_%s"%t]['eff_pt20_q12_3GeV'].GetTotalHistogram()
    toPlot[t] = ROOT.TEfficiency(thePass,theTotal)
    toPlot[t].SetLineColor(colors[t])
    toPlot[t].SetTitle(";Generated muon  p_{T} ;Efficiency")
    leg.AddEntry(toPlot[t],pretty[t],"l")
    toPlot[t].Draw()
    canvas9.Update()
    toPlot[t].GetPaintedGraph().SetMaximum(1.1)
  else:
    theAddPass = picks[t]["SingleMu_PU200_DP_%s"%t]['eff_pt20_q12_3GeV'].GetPassedHistogram()
    thePass = thePass + theAddPass
    toPlot[t] = ROOT.TEfficiency(thePass,theTotal)
    toPlot[t].SetLineColor(colors[t])
    leg.AddEntry(toPlot[t]," + " + pretty[t],"l")

  toPlot[t].Draw(" same")


leg.Draw("same")
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_pt_patternsplit_DispHighPt.pdf')
canvas9.SaveAs('~/www/omtf_2020/Jul27/SingleMu/tdr_pt_patternsplit_DispHighPt.png')
