from ROOT import TFile, gStyle, TCanvas, TH1F, TLegend, TArrow, TLatex, TPaveText

def set_pub_style():
  from ROOT import gStyle
  # No Canvas Border
  gStyle.SetCanvasBorderMode(0)
  gStyle.SetCanvasBorderSize(0)
  # White BG
  gStyle.SetCanvasColor(10)
  # Format for axes
  gStyle.SetLabelFont(42, 'xyz')
  gStyle.SetLabelSize(0.05, 'xyz')
  gStyle.SetLabelOffset(0.01, 'xyz')
  # gStyle->SetNdivisions(510, 'xyz')
  gStyle.SetTitleFont(42, 'xyz')
  gStyle.SetTitleColor(1, 'xyz')
  gStyle.SetTitleSize(0.06, 'xyz')
  gStyle.SetTitleOffset(1.25, 'xyz')
  # No pad borders
  gStyle.SetPadBorderMode(0)
  gStyle.SetPadBorderSize(0)
  # White BG
  gStyle.SetPadColor(10)
  # Margins for labels etc.
  gStyle.SetPadLeftMargin(0.155)
  gStyle.SetPadBottomMargin(0.24)
  gStyle.SetPadRightMargin(0.10)
  gStyle.SetPadTopMargin(0.12)
  # No error bars in x direction
  gStyle.SetErrorX(0)
  # Format legend
  gStyle.SetLegendBorderSize(0)

def set_prelim_style():
  from ROOT import gStyle
  gStyle.SetOptDate(0)
  gStyle.SetOptStat(0)
  gStyle.SetOptFit(0)
  gStyle.SetOptTitle(0)

def set_meeting_style():
  from ROOT import gStyle
  gStyle.SetOptDate(0)
  gStyle.SetOptTitle(0)
  gStyle.SetOptStat(1111)
  gStyle.SetStatBorderSize(1)
  gStyle.SetStatColor(10)
  gStyle.SetStatFont(42)
  gStyle.SetStatFontSize(0.03)
  gStyle.SetOptFit(1111)

def set_canvas_style(mbc):
  mbc.SetFillColor(0)
  # mbc.SetLeftMargin(0.15)
  # mbc.SetRightMargin(0.15)
  # mbc.SetTopMargin(0.05)
  # mbc.SetBottomMargin(0.05)
  mbc.SetLeftMargin(0.15)
  mbc.SetRightMargin(0.15)
  mbc.SetTopMargin(0.05)
  mbc.SetBottomMargin(0.18)

def format_data_hist(hist):
  hist.SetStats(0)
  hist.SetMarkerStyle(20)
  hist.SetMarkerSize(1)
  hist.SetLineWidth(2)
  hist.SetLineColor(1)

  hist.GetXaxis().SetNdivisions(509)
  hist.GetYaxis().SetNdivisions(504)
  hist.GetXaxis().SetLabelFont(42)
  hist.GetXaxis().SetTitleSize(0.07)
  hist.GetXaxis().SetTitleOffset(1.13)
  hist.GetXaxis().SetLabelOffset(0.02)
  hist.GetXaxis().SetLabelSize(0.07)
  hist.GetYaxis().SetLabelFont(42)
  hist.GetYaxis().SetTitleSize(0.07)
  hist.GetYaxis().SetTitleOffset(1.055)
  hist.GetYaxis().SetLabelOffset(0.01)
  hist.GetYaxis().SetLabelSize(0.07)

def name_axis(hist_graph, xname = '', yname = ''):
    if xname:
        hist_graph.GetXaxis().SetTitle(xname)
        hist_graph.GetXaxis().CenterTitle()
    if yname:
        hist_graph.GetYaxis().SetTitle(yname)
        hist_graph.GetYaxis().CenterTitle()

def format_mc_hist(h_mc, color, style = 3001):
    h_mc.SetLineColor(color)
    h_mc.SetLineWidth(2)
    if style != -1:
        h_mc.SetFillStyle(style)
        h_mc.SetFillColor(color)

def set_legend(histlist, namelist, stylelist, x1, y1, x2, y2, font = 1, size = 0.03):
    if len(histlist) != len(namelist) or len(histlist) != len(stylelist):
        print ('legend listerror')
        exit

    leg=TLegend(x1, y1, x2, y2)
    for j in range(len(histlist)):
        leg.AddEntry(histlist[j], namelist[j], stylelist[j])

    leg.SetFillColor(0)
    leg.SetTextFont(font)
    leg.SetTextSize(size)
    leg.SetBorderSize(0)
    return leg

def set_pavetext(x1, y1, x2, y2, color, size, *title):
    pt = TPaveText(x1, y1, x2, y2, 'BRNDC')
    pt.SetBorderSize(0)
    pt.SetFillColor(10)
    pt.SetFillStyle(0)
    pt.SetTextAlign(12)
    pt.SetTextSize(size)  #0.06
    pt.SetLineColor(0)
    pt.SetTextColor(color)
    if not isinstance(title, list):
        title = list(title)
    for t in title:
        pt.AddText(t)
    return pt

def set_yzero_hist(histlist):
	histlist.GetYaxis().SetRangeUser(0, 1.3 * histlist.GetMaximum())

def position_convert(x, xmin, xmax):
    pos = 0.15 + 0.7 * (x - xmin) / (xmax - xmin)
    return pos

def set_scale_hist(hist1, hist2):
    hist2.Scale(1.0 * hist1.GetMaximum()/hist2.GetMaximum(), 'nosw2')
    hist1.Sumw2()

def set_ellipse(el, fill_color = 0, line_color = 4, line_width = 6, fill_style = 0):
    el.SetFillColor(fill_color)
    el.SetFillStyle(fill_style)
    el.SetLineColor(line_color)
    el.SetLineWidth(line_width)

def set_graph_style(gr, xtitle, ytitle):
    # gr.GetXaxis().SetNdivisions(509)
    # gr.GetYaxis().SetNdivisions(504)
    # gr.SetLineWidth(2)
    # gr.SetLineWidth(2)
    # gr.GetXaxis().SetLabelFont(42)
    # gr.GetXaxis().SetTitleSize(0.07)
    # gr.GetXaxis().SetTitleOffset(1.13)
    # gr.GetXaxis().SetLabelOffset(0.02)
    # gr.GetXaxis().SetLabelSize(0.07)
    # gr.GetYaxis().SetLabelFont(42)
    # gr.GetYaxis().SetTitleSize(0.07)
    # gr.GetYaxis().SetTitleOffset(1.01)
    # gr.GetYaxis().SetLabelOffset(0.01)
    # gr.GetYaxis().SetLabelSize(0.07)
    # gr.GetXaxis().SetTitle(xtitle)
    # gr.GetXaxis().CenterTitle()
    # gr.GetYaxis().SetTitle(ytitle)
    # gr.GetYaxis().CenterTitle()
    # gr.SetMarkerStyle(20)
    # gr.SetMarkerSize(1)
    # gr.SetLineColor(1)

    gr.GetXaxis().SetNdivisions(504)
    gr.GetYaxis().SetNdivisions(503)
    gr.SetLineWidth(2)
    gr.SetLineWidth(2)
    gr.GetXaxis().SetLabelFont(42)
    gr.GetXaxis().SetTitleSize(0.09)
    gr.GetXaxis().SetTitleOffset(1.115)
    gr.GetXaxis().SetLabelOffset(0.02)
    gr.GetXaxis().SetLabelSize(0.09)
    gr.GetYaxis().SetLabelFont(42)
    gr.GetYaxis().SetTitleSize(0.09)
    gr.GetYaxis().SetTitleOffset(0.95)
    gr.GetYaxis().SetLabelOffset(0.01)
    gr.GetYaxis().SetLabelSize(0.09)
    gr.GetXaxis().SetTitle(xtitle)
    gr.GetXaxis().CenterTitle()
    gr.GetYaxis().SetTitle(ytitle)
    gr.GetYaxis().CenterTitle()
    gr.SetMarkerStyle(20)
    gr.SetMarkerSize(1)
    gr.SetLineColor(1)

def format_data_graph(graph):
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(1)
    graph.SetLineWidth(2)

    graph.GetXaxis().SetNdivisions(509)
    graph.GetYaxis().SetNdivisions(504)
    graph.GetXaxis().SetLabelFont(42)
    graph.GetXaxis().SetTitleSize(0.07)
    graph.GetXaxis().SetTitleOffset(1.05)
    graph.GetXaxis().SetLabelOffset(0.01)
    graph.GetXaxis().SetLabelSize(0.07)
    graph.GetYaxis().SetLabelFont(42)
    graph.GetYaxis().SetTitleSize(0.07)
    graph.GetYaxis().SetTitleOffset(0.98)
    graph.GetYaxis().SetLabelOffset(0.01)
    graph.GetYaxis().SetLabelSize(0.07)

def set_arrow(x1, y1, x2, y2, arr_size, line_width, linestyle, color):
  arr = TArrow(x1, y1, x2, y2, arr_size, linestyle)
  arr.SetLineColor(color)
  arr.SetLineWidth(line_width)
  return arr

# FormatData : 20, 1, 1, 2
def SetHistDot(hist, style, size, color, width):
  hist.SetMarkerStyle(style)
  hist.SetMarkerSize(size)
  hist.SetLineWidth(width)
  hist.SetMarkerColor(color)

# FormatMC1 : 2, 2
# FormatMC3 : 6, 2
def SetHistLine(hist, color, width):
  hist.SetLineWidth(width)
  hist.SetLineColor(color)

# FormatMC2 : 4, 2, 3001
def SetHistFill(hist, color, width, fillstyle):
  hist.SetLineColor(color)
  hist.SetFillColor(color)
  hist.SetLineWidth(width)
  hist.SetFillStyle(fillstyle)

# Add
def SetLatex(xm, ym, name):
  t0 = TLatex(xm, ym, name)
  t0.SetTextAlign(22)
  t0.SetTextColor(2)
  t0.SetTextFont(63)
  t0.SetTextSize(30)
  t0.SetLineWidth(2)
  return t0

# Write "BESIII" in the upper right corner
def WriteBes3():
  bes3 = TLatex(0.94, 0.94, 'BESIII')
  bes3.SetNDC()
  bes3.SetTextFont(72)
  bes3.SetTextSize(0.1)
  bes3.SetTextAlign(33)
  return bes3

# Write "Preliminary" below BESIII to be used together with WriteBes3()
def WritePreliminary():
  prelim = TLatex(0.94, 0.86, 'Preliminary')
  prelim.SetNDC()
  prelim.SetTextFont(62)
  prelim.SetTextSize(0.055)
  prelim.SetTextAlign(33)
  return prelim

# ---------------------------------- Add ---------------------------------------#
def SetYMaximumHist(histlist):
  temp_max = -1
  index_max = -1
  for j in range(len(histlist)):
    if temp_max < histlist[j].GetMaximum():
      temp_max = histlist[j].GetMaximum()
      index_max = j

  histlist[0].GetYaxis().SetRangeUser(0, 1.2 * temp_max)

def set_xframe_style(xframe, xtitle, ytitle):
  xframe.GetXaxis().SetTitle(xtitle)
  xframe.GetXaxis().SetTitleSize(0.06)
  xframe.GetXaxis().SetLabelSize(0.06)
  xframe.GetXaxis().SetTitleOffset(1.05)
  xframe.GetXaxis().SetLabelOffset(0.008)
  xframe.GetXaxis().SetNdivisions(508)
  xframe.GetXaxis().CenterTitle()
  xframe.GetYaxis().SetNdivisions(504)
  xframe.GetYaxis().SetTitleSize(0.06)
  xframe.GetYaxis().SetLabelSize(0.06)
  xframe.GetYaxis().SetTitleOffset(0.8)
  xframe.GetYaxis().SetLabelOffset(0.008)
  xframe.GetYaxis().SetTitle(ytitle)
  xframe.GetYaxis().CenterTitle()


