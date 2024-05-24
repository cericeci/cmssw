from DataFormats.FWLite import Events, Handle
import numpy as np
import sys
import ROOT

ROOT.gStyle.SetOptStat(False)
vertHandle, vertLabel = Handle("vector<reco::Vertex>"), ("offlinePrimaryVertices","WithBS","PV")

fil1 = Events(sys.argv[1])
fil2 = Events(sys.argv[2])
tag1 = sys.argv[3]
tag2 = sys.argv[4]

out1 = {}
out2 = {}

theVars       = {"x": lambda x: x.x(), "y": lambda x: x.y(), "z": lambda x: x.z()}
minx, maxx = 9999, -9999
miny, maxy = 9999, -9999
minz, maxz = 9999, -9999

for iev, ev in enumerate(fil1):
  evDic = []
  ev.getByLabel(vertLabel,vertHandle)
  vertex= vertHandle.product()
  for v in vertex:
    d = {var: theVars[var](v) for var in theVars}
    evDic.append(d)
    if v.x() < minx: minx = v.x()
    if v.x() > maxx: maxx = v.x()
    if v.y() < miny: miny = v.y()
    if v.y() > maxy: maxy = v.y()
    if v.z() < minz: minz = v.z()
    if v.z() > maxz: maxz = v.z()
    
  out1[iev]= evDic
  print(iev)
  #if iev >= 3: break

th2X = ROOT.TH2F("x", "x", 40, minx, maxx, 40, minx, maxx)
th2Y = ROOT.TH2F("y", "y", 40, miny, maxy, 40, miny, maxy)
th2Z = ROOT.TH2F("z", "z", 40, minz, maxz, 40, minz, maxz)


for iev in out1:
  for v in out1[iev]:
    th2X.Fill(v["x"], v["x"])
    th2Y.Fill(v["y"], v["y"])
    th2Z.Fill(v["z"], v["z"])

for var in ["x", "y", "z"]:
  c1 = ROOT.TCanvas("c","c",800, 600)
  c1.SetRightMargin(0.2)
  c1.SetLeftMargin(0.15)
  c1.SetTopMargin(0.05)
  c1.SetBottomMargin(0.15)
  h = None
  if var == "x": h = th2X.Clone("X")
  if var == "y": h = th2Y.Clone("Y")
  if var == "z": h = th2Z.Clone("Z")
 
  h.GetZaxis().SetTitle("Vertices")
  h.GetZaxis().SetTitleOffset(1.8)
  h.GetYaxis().SetTitle("Algo %s %s [cm]"%(tag1, var))
  h.GetXaxis().SetTitle("Algo %s %s [cm]"%(tag2, var))
  h.SetTitle("")
  h.Draw("colz")
  c1.SaveAs(var + ".pdf")


"""for iev, ev in enumerate(fil2):
  evDic = []
  ev.getByLabel(vertLabel,vertHandle)
  vertex= vertHandle.product()
  for v in vertex:
    d = {var: theVars[var](v) for var in theVars}
    evDic.append(d)
  out2[iev] = evDic
  if iev >= 3: break

print(out1, out2)
"""
