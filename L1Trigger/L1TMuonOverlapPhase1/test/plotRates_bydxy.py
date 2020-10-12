import pickle
import math
import ROOT

pileups = [200]
ss = ["Nu_PU140_DP","Nu_PU200_DP","Nu_PU250_DP"]
samples = {"Nu_PU140_DP":ROOT.kBlue,"Nu_PU200_DP":ROOT.kRed,"Nu_PU250_DP":ROOT.kBlack}
tags = {"Nu_PU140_DP":"PU 140","Nu_PU200_DP":"PU 200","Nu_PU250_DP":"PU 250"}
qualities = ['_q12']
ROOT.gROOT.SetBatch(True)

#ROOT.gROOT.ProcessLine('.L /nfs/fanae/user/carlosec/OMTF_2020/CMSSW_11_1_0_pre6/src/L1Trigger/L1TMuonOverlapPhase1/test/PlotTemplate.C+')

with open('tdr_rates_bydxy.pickle', 'rb') as handle:
    bb = pickle.load(handle)

outFile = ROOT.TFile("tdr_rates_bydxy.root","RECREATE")
outFile.cd()

bins=  [0,0.1,0.2,0.3,0.4]

cbins = []
for i in range(len(bins)-1):
    cbins.append((bins[i] + bins[i+1])/2.)


coeff = 2760*11.246

hp = ROOT.TH1F('hp','',1,-0.5,0.5)
ht = ROOT.TH1F('ht','',1,-0.5,0.5)

for puValue in pileups:
 gr = {}
 canvas = ROOT.TCanvas("c1","c1",800,600) #CreateCanvas('name',True,True)
 leg = ROOT.TLegend(0.55,0.65,0.9,0.85)
 drawn = False
 for s in ss:
   for q in qualities:
      puHandle = ''
      if puValue == 0: puHandle ='NOPU'
      else: puHandle = 'PU' + str(puValue)
      gr[s]      = ROOT.TGraphAsymmErrors(len(bins)-1)
      for i, b in enumerate(cbins):
          hp.SetBinContent(1, bb[s]['fired'+str(bins[i])+ q] )
          ht.SetBinContent(1, bb[s]['total'] )
          eff = ROOT.TEfficiency(hp, ht)
          val    = coeff * eff.GetEfficiency(1)
          val_up = coeff * eff.GetEfficiencyErrorUp(1)
          val_dn = coeff * eff.GetEfficiencyErrorLow(1)

          gr[s].SetPoint(i, b, val)
          gr[s].SetPointEYlow(i, val_dn)
          gr[s].SetPointEYhigh(i, val_up)
          gr[s].SetPointEXlow(i, b - bins[i])
          gr[s].SetPointEXhigh(i, bins[i+1] - b)
          print s, b, val
      #Set drawing options and draw the gr[s]aph
      #canvas.SetLogx(True)
      gr[s].SetMarkerColor(samples[s])
      gr[s].SetLineColor(samples[s])
      gr[s].SetMaximum(1000)
      gr[s].GetXaxis().SetLimits(0,0.4)
      gr[s].GetXaxis().SetTitle("L1 |d_{xy}^{cut}| [m]")
      gr[s].GetYaxis().SetTitle("Rate [kHz]")
      gr[s].SetTitle("")
      if not(drawn):
        gr[s].Draw("AP")
        drawn = True
      else:
        gr[s].Draw("P same")
      leg.AddEntry(gr[s],tags[s],'l')
 leg.Draw("same")
 #ROOT.DrawPrelimLabel(canvas)
 #ROOT.DrawLumiLabel(canvas,'14 TeV, %i PU'%puValue)
 #ROOT.SaveCanvas(canvas,'tdr_dxy_rate'+ q + '_PU_log' + str(puValue))
 canvas.SaveAs("/nfs/fanae/user/carlosec/www/omtf_2020/Jul27/Rates/tdr_rate_bydxy.pdf")
 canvas.SaveAs("/nfs/fanae/user/carlosec/www/omtf_2020/Jul27/Rates/tdr_rate_bydxy.png")
outFile.Close()
