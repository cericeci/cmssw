import pickle
import math
import ROOT
import os
pileups = [0]#[0,140,200]#200]#,300]
modes   = ["AP","DP","BOTH","AP_newEta","DP_newEta", "BOTH_newEta"]
qualities = ['_q12']
types = ['Disp_pt30']
outFile = ROOT.TFile("tdr_eff.root","RECREATE")
outFile.cd()

ROOT.gROOT.SetBatch(True)

for puValue in pileups:
 for mode in modes:
  for typ in types:
   for q in qualities:
      print puValue, mode, typ, q
      canvas = ROOT.TCanvas("c1","c1",800,600) #CreateCanvas('name',False,True)
      puHandle = ''
      if puValue == 0: puHandle ='NoPU' if "Disp" in typ else "NOPU"
      else: puHandle = 'PU' + str(puValue)
      puHandle += "_"+mode
      dataset = typ + "_" + mode #+ puHandle
      #print 'tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+".pickle")
      #if not(os.path.exists('tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+".pickle"))): continue
      with open('tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+  ".pickle"), 'rb') as handle:
        b = pickle.load(handle)
        print 'tdr_eff_SingleMu.pickle'.replace(".pickle",dataset + ".pickle")
      for charge in ["5GeV","3GeV","2GeV","1GeV"]:
            b[dataset]['eff_pt0' + q + "_" + charge].SetName('eff_pt3' + q + "_" + charge + puHandle)
            b[dataset]['eff_pt3'+ q + "_" + charge].SetName('eff_pt10' + q + "_" + charge + puHandle)
            b[dataset]['eff_pt10'+ q + "_" + charge].SetName('eff_pt10' + q + "_" + charge + puHandle)

            b[dataset]['eff_pt0' + q + "_" + charge].Write()
            b[dataset]['eff_pt3'+ q + "_" + charge].Write()
            b[dataset]['eff_pt10'+ q + "_" + charge].Write()
            b[dataset]['eff_pt0'+ q + "_" + charge].Draw()
            b[dataset]['eff_pt0'+ q + "_" + charge].SetTitle(';Generated muon p_{T} [GeV];Efficiency')
            b[dataset]['eff_pt3'+ q+ "_" + charge].Draw("same")
            b[dataset]['eff_pt10'+ q+ "_" + charge].Draw("same")
            b[dataset]['eff_pt0'+ q + "_" + charge].SetLineColor(ROOT.kRed)
            b[dataset]['eff_pt3'+ q+ "_" + charge].SetLineColor(ROOT.kBlue)
            b[dataset]['eff_pt10'+ q+ "_" + charge].SetLineColor(ROOT.kGreen)
            b[dataset]['eff_pt0'+ q + "_" + charge].SetMarkerStyle(8)
            b[dataset]['eff_pt3'+ q+ "_" + charge].SetMarkerStyle(23)
            b[dataset]['eff_pt10'+ q+ "_" + charge].SetMarkerStyle(33)
            b[dataset]['eff_pt0'+ q + "_" + charge].SetMarkerColor(ROOT.kRed)
            b[dataset]['eff_pt3'+ q+ "_" + charge].SetMarkerColor(ROOT.kBlue)
            b[dataset]['eff_pt10'+ q+ "_" + charge].SetMarkerColor(ROOT.kGreen)

            b[dataset]['eff_pt0'+ q + "_" + charge].SetMarkerSize(1.2)
            b[dataset]['eff_pt3'+ q+ "_" + charge].SetMarkerSize(1.5)
            b[dataset]['eff_pt10'+ q+ "_" + charge].SetMarkerSize(1.5)


            b[dataset]['eff_pt0'+ q + "_" + charge].SetLineWidth(2)
            b[dataset]['eff_pt3'+ q+ "_" + charge].SetLineWidth(2)
            b[dataset]['eff_pt10'+ q+ "_" + charge].SetLineWidth(2)


            leg = ROOT.TLegend(0.5,0.65,0.9,0.36);
            leg.SetTextSize(0.035);
            leg.AddEntry(b[dataset]['eff_pt0'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 0 GeV','l');
            leg.AddEntry(b[dataset]['eff_pt3'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 3 GeV','l');
            leg.AddEntry(b[dataset]['eff_pt10'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 10 GeV','l');

            leg.Draw("same")
            canvas.SaveAs('~/www/omtf_2020/Oct06/tdr_pt_eff'+ dataset + "_" + charge+".pdf")
            canvas.SaveAs('~/www/omtf_2020/Oct06/tdr_pt_eff'+ dataset + "_" + charge+".png")

      
      canvas2 = ROOT.TCanvas("c2","c2", 800,600)# CreateCanvas('name2',False,True)
      canvas2.cd()
      b[dataset]['hEta0_q12_cut0'].SetName("hEta0_q12_cut0" + puHandle)
      b[dataset]['hEta0_q12_cut0'].Write()
      b[dataset]['hEta0_q12_cut0'].Draw()
      canvas2.Update()
      graph = b[dataset]['hEta0_q12_cut0'].GetPaintedGraph()
      graph.GetXaxis().SetRangeUser(0.,2.4)
      b[dataset]['hEta0_q12_cut0'].SetTitle(';Generated muon  #eta;Efficiency')
      l1 = ROOT.TLine(0.82,0,0.82,1)
      l2 = ROOT.TLine(-0.82,0,-0.82,1)
      l3 = ROOT.TLine(1.23,0,1.23,1)
      l4 = ROOT.TLine(-1.23,0,-1.23,1)
      l1.SetLineWidth(2)
      l1.SetLineStyle(10)
      l1.SetLineColor(ROOT.kRed)

      l2.SetLineWidth(2)
      l2.SetLineStyle(10)
      l2.SetLineColor(ROOT.kRed)

      l3.SetLineWidth(2)
      l3.SetLineStyle(10)
      l3.SetLineColor(ROOT.kRed)

      l4.SetLineWidth(2)
      l4.SetLineStyle(10)
      l4.SetLineColor(ROOT.kRed)


      l1.Draw("same")
      l2.Draw("same")
      l3.Draw("same")
      l4.Draw("same")


      leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
      leg.SetTextSize(0.035);
      leg.SetHeader('#splitline{p_{T}^{gen muon} #geq 30 GeV}{p_{T}^{L1 muon} #geq 0 GeV}')
      leg.Draw("same")
      canvas2.SaveAs('~/www/omtf_2020/Oct06/tdr_eta25_eff06'+ dataset+".pdf")
      canvas2.SaveAs('~/www/omtf_2020/Oct06/tdr_eta25_eff06'+ dataset+".png")

      canvas9 = ROOT.TCanvas("c4","c4",800,600) #CreateCanvas('name8',False,True)
      canvas9.cd()
      b[dataset]['hDxy_q12_10steps'].SetName("hDxy_q12_10steps"+ puHandle)
      b[dataset]['hDxy_q12_10steps'].Write()
      b[dataset]['hDxy_q12_10steps'].Draw()
      b[dataset]['hDxy_q12_10steps'].SetTitle(';Generated muon  d_{xy};Efficiency')


      leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
      leg.SetTextSize(0.025);
      leg.SetHeader('No cuts in L1 or gen')

      leg.Draw("same")
      canvas9.SaveAs('~/www/omtf_2020/Oct06/tdr_dxy_'+ dataset+".pdf")
      canvas9.SaveAs('~/www/omtf_2020/Oct06/tdr_dxy_'+ dataset+".png")


outFile.Close()
