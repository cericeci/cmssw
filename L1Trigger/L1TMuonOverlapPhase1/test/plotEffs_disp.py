import pickle
import math
import ROOT
import os
pileups = [200]#[0,140,200]#200]#,300]
modes   = ["DP"]#["DP","SP"]
qualities = ['_q12']
types = ['Disp_HighPt_','SingleMu_']
outFile = ROOT.TFile("tdr_eff.root","RECREATE")
outFile.cd()

ROOT.gROOT.SetBatch(True)

for puValue in pileups:
 for mode in modes:
  for typ in types:
   for q in qualities:
      canvas = ROOT.TCanvas("c1","c1",800,600) #CreateCanvas('name',False,True)
      puHandle = ''
      if puValue == 0: puHandle ='NoPU' if "Disp" in typ else "NOPU"
      else: puHandle = 'PU' + str(puValue)
      puHandle += "_"+mode
      dataset = typ + puHandle
      print dataset
      if not(os.path.exists('tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+".pickle"))): continue
      with open('tdr_eff_SingleMu.pickle'.replace(".pickle",dataset+".pickle"), 'rb') as handle:
        b = pickle.load(handle)

      for charge in ["5GeV","3GeV","2GeV","1GeV"]:
            b[typ + puHandle]['eff_pt3' + q + "_" + charge].SetName('eff_pt3' + q + "_" + charge + puHandle)
            b[typ + puHandle]['eff_pt10'+ q + "_" + charge].SetName('eff_pt10' + q + "_" + charge + puHandle)
            b[typ + puHandle]['eff_pt20'+ q + "_" + charge].SetName('eff_pt20' + q + "_" + charge + puHandle)

            b[typ + puHandle]['eff_pt3' + q + "_" + charge].Write()
            b[typ + puHandle]['eff_pt10'+ q + "_" + charge].Write()
            b[typ + puHandle]['eff_pt20'+ q + "_" + charge].Write()
            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].Draw()
            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetTitle(';Generated muon p_{T} [GeV];Efficiency')
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].Draw("same")
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].Draw("same")
            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetLineColor(ROOT.kRed)
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].SetLineColor(ROOT.kBlue)
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].SetLineColor(ROOT.kGreen)
            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetMarkerStyle(8)
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].SetMarkerStyle(23)
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].SetMarkerStyle(33)
            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetMarkerColor(ROOT.kRed)
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].SetMarkerColor(ROOT.kBlue)
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].SetMarkerColor(ROOT.kGreen)

            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetMarkerSize(1.2)
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].SetMarkerSize(1.5)
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].SetMarkerSize(1.5)


            b[typ + puHandle]['eff_pt3'+ q + "_" + charge].SetLineWidth(2)
            b[typ + puHandle]['eff_pt10'+ q+ "_" + charge].SetLineWidth(2)
            b[typ + puHandle]['eff_pt20'+ q+ "_" + charge].SetLineWidth(2)


            leg = ROOT.TLegend(0.5,0.65,0.9,0.36);
            leg.SetTextSize(0.035);
            leg.AddEntry(b[typ + puHandle]['eff_pt3'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 3 GeV','l');
            leg.AddEntry(b[typ + puHandle]['eff_pt10'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 10 GeV','l');
            leg.AddEntry(b[typ + puHandle]['eff_pt20'+ q+ "_" + charge],'p_{T}^{L1 muon} #geq 20 GeV','l');

            #ROOT.DrawPrelimLabel(canvas)
            #ROOT.DrawLumiLabel(canvas,'%i PU'%puValue)
            leg.Draw("same")
            canvas.SaveAs('~/www/omtf_2020/Sep23/Displaced/tdr_pt_eff'+ dataset + "_" + charge+".pdf")
            canvas.SaveAs('~/www/omtf_2020/Sep23/Displaced/tdr_pt_eff'+ dataset + "_" + charge+".png")

            #ROOT.SaveAsCanvas(canvas,'~/www/omtf_2020/Jul27/Displaced/tdr_pt_eff'+ q + str(puHandle)+ "_" + charge)
      
      canvas2 = ROOT.TCanvas("c2","c2", 800,600)# CreateCanvas('name2',False,True)
      canvas2.cd()
      b[typ + puHandle]['hEta20_q12_cut20'].SetName("hEta20_q12_cut20" + puHandle)
      b[typ + puHandle]['hEta20_q12_cut20'].Write()
      b[typ + puHandle]['hEta20_q12_cut20'].Draw()
      canvas2.Update()
      graph = b[typ + puHandle]['hEta20_q12_cut20'].GetPaintedGraph()
      graph.GetXaxis().SetRangeUser(0.,2.4)
      #graph.GetXaxis().SetMaximum(2.)
      #canvas2.Update()
      #graph = b[typ + puHandle]['hEta20_q12_cut20'].GetPaintedGraph()
      #graph.SetMinimum(0.6)
      #graph.SetMaximum(1.01)
      b[typ + puHandle]['hEta20_q12_cut20'].SetTitle(';Generated muon  #eta;Efficiency')
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
      leg.SetHeader('p_{T}^{gen muon} #geq 25 GeV')
      leg.Draw("same")
      canvas2.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_eta25_eff06'+ dataset+".pdf")
      canvas2.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_eta25_eff06'+ dataset+".png")

      #ROOT.DrawPrelimLabel(canvas2)
      #ROOT.DrawLumiLabel(canvas2,'%i PU'%puValue)
      #ROOT.SaveAsCanvas(canvas2,'~/www/omtf_2020/Jul27/Displaced/tdr_eta25_eff06'+ q+ str(puHandle))

      canvas8 = ROOT.TCanvas("c3","c3",800,600) #CreateCanvas('name8',False,True)
      canvas8.cd()
      b[typ + puHandle]['hEta7_15_q12_cut5'].SetName("hEta7_15_q12_cut5"+ puHandle)
      b[typ + puHandle]['hEta7_15_q12_cut5'].Write()
      b[typ + puHandle]['hEta7_15_q12_cut5'].Draw()
      b[typ + puHandle]['hEta7_15_q12_cut5'].SetTitle(';Generated muon  #eta;Efficiency')
      canvas8.Update()
      graph = b[typ + puHandle]['hEta7_15_q12_cut5'].GetPaintedGraph()
      graph.GetXaxis().SetRangeUser(0.,2.4)

      #canvas8.Update()

      #graph = b[typ + puHandle]['hEta7_15_q12_cut5'].GetPaintedGraph()
      ##graph.SetMinimum(0.6)
      ##graph.SetMaximum(1.01)
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
      leg.SetTextSize(0.025);
      leg.SetHeader('7 GeV #leq p_{T}^{gen muon} #leq 15 GeV')

      leg.Draw("same")
      canvas8.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_eta7_15_c5_eff'+ q + dataset+".pdf")
      canvas8.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_eta7_15_c5_eff'+ q + dataset+".png")

      #ROOT.DrawPrelimLabel(canvas8)
      #ROOT.DrawLumiLabel(canvas8,'%i PU'%puValue)
      #ROOT.SaveAsCanvas(canvas8,'~/www/omtf_2020/Jul27/Displaced/tdr_eta7_15_c5_eff'+ q + str(puHandle))
      
      canvas9 = ROOT.TCanvas("c4","c4",800,600) #CreateCanvas('name8',False,True)
      canvas9.cd()
      b[typ + puHandle]['hDxy_q12_10steps'].SetName("hDxy_q12_10steps"+ puHandle)
      b[typ + puHandle]['hDxy_q12_10steps'].Write()
      b[typ + puHandle]['hDxy_q12_10steps'].Draw()
      b[typ + puHandle]['hDxy_q12_10steps'].SetTitle(';Generated muon  d_{xy};Efficiency')


      leg = ROOT.TLegend(0.55,0.6,0.85,0.48);
      leg.SetTextSize(0.025);
      leg.SetHeader('No cuts in L1 or gen')

      leg.Draw("same")
      canvas9.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_dxy_'+ dataset+".pdf")
      canvas9.SaveAs('~/www/omtf_2020/Jul27/Displaced/tdr_dxy_'+ dataset+".png")


outFile.Close()
