#!/usr/bin/env python
'''
Fit to mass of Kppim and pKmpip
'''

__author__ = 'Maoqiang JING <jingmq@ihep.ac.cn>'
__copyright__ = 'Copyright (c) Maoqiang JING'
__created__ = '[2024-08-27 Tue 18:52]'

import math
from array import array
import ROOT, sys, os
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
import logging
from math import *
from ROOT import *
import random
sys.path.append('../')
from tools import set_pub_style, set_prelim_style, format_data_hist, set_pavetext, name_axis, set_canvas_style, set_yzero_hist, set_legend
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def usage():
    sys.stdout.write('''
NAME
    fit_m_Kppim_m_pKmpip.py

SYNOPSIS
    ./fit_m_Kppim_m_pKmpip.py

AUTHOR
    Maoqiang JING <jingmq@ihep.ac.cn>

DATE
    August 2024
\n''')

set_pub_style()
set_prelim_style()
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadBottomMargin(0.18)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)

def make_hist_m_Kppim(t):
    h = TH1F('h_m_Kppim', 'h_m_Kppim', xbins, xmin, xmax)
    for idx, evt in enumerate(t):
        h.Fill(evt.m_Kppim)
    return h

def make_hist_m_pKmpip(t):
    h = TH1F('h_m_pKmpip', 'h_m_pKmpip', ybins, ymin, ymax)
    for idx, evt in enumerate(t):
        h.Fill(evt.m_pKmpip)
    return h

def fit(data, sig_path):
    mi = FSModeInfo('p+ K+ K- pi+ pi-')
    mc = str(mi.modeString())
    tree_name = 'ntFSGlueX_MODECODE'.replace('MODECODE', mc)
    try:
        f_data = TFile(data[0])
        t_data = f_data.Get(tree_name)
        entries_data = t_data.GetEntries()
        logging.info('Entries :'+str(entries_data))
    except:
        logging.error(data[0] + 'is invalid!')

    try:
        f_sig = TFile(sig_path)
        t_sig = f_sig.Get(tree_name)
        entries_sig = t_sig.GetEntries()
        logging.info('Entries :'+str(entries_sig))
    except:
        logging.error(sig_path + 'is invalid!')

    global xmin, xmax, xbins, ymin, ymax, ybins
    xmin, xmax = 1.7, 2.0
    xbins = int((xmax - xmin) / 0.002)
    ymin, ymax = 2.2, 2.35
    ybins = int((ymax - ymin) / 0.002)

    m_Kppim  = RooRealVar('m_Kppim', 'm_Kppim', xmin, xmax)
    m_pKmpip = RooRealVar('m_pKmpip', 'm_pKmpip', ymin, ymax)
    m_Kppim.setBins(xbins, 'cache')
    m_pKmpip.setBins(ybins, 'cache')
    data_set = RooDataSet('dataset', 'dataset', {m_Kppim, m_pKmpip}, Import = t_data)

    '''
    signal pdf
    '''

    h_m_Kppim      = make_hist_m_Kppim(t_sig)
    hist_m_Kppim   = RooDataHist('hist_m_Kppim', 'hist_m_Kppim', [m_Kppim], Import = h_m_Kppim)
    sigpdf_m_Kppim = RooHistPdf('pdf_m_Kppim', 'pdf_m_Kppim', {m_Kppim}, hist_m_Kppim, 2)
    
    h_m_pKmpip      = make_hist_m_pKmpip(t_sig)
    hist_m_pKmpip   = RooDataHist('hist_m_pKmpip', 'hist_m_pKmpip', [m_pKmpip], Import = h_m_pKmpip)
    sigpdf_m_pKmpip = RooHistPdf('pdf_m_pKmpip', 'pdf_m_pKmpip', {m_pKmpip}, hist_m_pKmpip, 2)

    '''
    background pdf
    '''

    p0_m_Kppim     = RooRealVar('p0_m_Kppim', 'p0_m_Kppim', 0., -10, 10)
    p1_m_Kppim     = RooRealVar('p1_m_Kppim', 'p1_m_Kppim', 0., -10, 10)
    p2_m_Kppim     = RooRealVar('p2_m_Kppim', 'p2_m_Kppim', 0., -10, 10)
    bkgpdf_m_Kppim = RooChebychev('bkgpdf_m_Kppim', 'bkgpdf_m_Kppim', m_Kppim, [p0_m_Kppim])

    p0_m_pKmpip     = RooRealVar('p0_m_pKmpip', 'p0_m_pKmpip', 0., -10, 10)
    p1_m_pKmpip     = RooRealVar('p1_m_pKmpip', 'p1_m_pKmpip', 0., -10, 10)
    p2_m_pKmpip     = RooRealVar('p2_m_pKmpip', 'p2_m_pKmpip', 0., -10, 10)
    bkgpdf_m_pKmpip = RooChebychev('bkgpdf_m_pKmpip', 'bkgpdf_m_pKmpip', m_pKmpip, [p0_m_pKmpip])

    '''
    construct pdf
    '''

    sigpdf_m_Kppim_sigpdf_m_pKmpip     = RooProdPdf('sigpdf_m_Kppim_sigpdf_m_pKmpip', 'sigpdf_m_Kppim_sigpdf_m_pKmpip', sigpdf_m_Kppim, sigpdf_m_pKmpip)
    num_sigpdf_m_Kppim_sigpdf_m_pKmpip = RooRealVar('num_sigpdf_m_Kppim_sigpdf_m_pKmpip', 'num_sigpdf_m_Kppim_sigpdf_m_pKmpip', 10, 0, 3000)

    sigpdf_m_Kppim_bkgpdf_m_pKmpip     = RooProdPdf('sigpdf_m_Kppim_bkgpdf_m_pKmpip', 'sigpdf_m_Kppim_bkgpdf_m_pKmpip', sigpdf_m_Kppim, bkgpdf_m_pKmpip)
    num_sigpdf_m_Kppim_bkgpdf_m_pKmpip = RooRealVar('num_sigpdf_m_Kppim_bkgpdf_m_pKmpip', 'num_sigpdf_m_Kppim_bkgpdf_m_pKmpip', 10, 0, 30000)

    bkgpdf_m_Kppim_sigpdf_m_pKmpip     = RooProdPdf('bkgpdf_m_Kppim_sigpdf_m_pKmpip', 'bkgpdf_m_Kppim_sigpdf_m_pKmpip', bkgpdf_m_Kppim, sigpdf_m_pKmpip)
    num_bkgpdf_m_Kppim_sigpdf_m_pKmpip = RooRealVar('num_bkgpdf_m_Kppim_sigpdf_m_pKmpip', 'num_bkgpdf_m_Kppim_sigpdf_m_pKmpip', 10, 0, 30000)

    bkgpdf_m_Kppim_bkgpdf_m_pKmpip     = RooProdPdf('bkgpdf_m_Kppim_bkgpdf_m_pKmpip', 'bkgpdf_m_Kppim_bkgpdf_m_pKmpip', bkgpdf_m_Kppim, bkgpdf_m_pKmpip)
    num_bkgpdf_m_Kppim_bkgpdf_m_pKmpip = RooRealVar('num_bkgpdf_m_Kppim_bkgpdf_m_pKmpip', 'num_bkgpdf_m_Kppim_bkgpdf_m_pKmpip', 10, 0, 30000)

    while True:
        model = RooAddPdf(
            'model',
            'model',
            [
                sigpdf_m_Kppim_sigpdf_m_pKmpip,
                sigpdf_m_Kppim_bkgpdf_m_pKmpip,
                bkgpdf_m_Kppim_sigpdf_m_pKmpip,
                bkgpdf_m_Kppim_bkgpdf_m_pKmpip,
            ],
            [
                num_sigpdf_m_Kppim_sigpdf_m_pKmpip,
                num_sigpdf_m_Kppim_bkgpdf_m_pKmpip,
                num_bkgpdf_m_Kppim_sigpdf_m_pKmpip,
                num_bkgpdf_m_Kppim_bkgpdf_m_pKmpip,
            ]
        )

        results = model.fitTo(data_set, RooFit.Save(kTRUE), RooFit.Extended(kTRUE))

        # plot results
        if not os.path.exists('./figs/'):
            os.makedirs('./figs/')

        c1 = TCanvas('c1', 'c1', 1000, 700)
        set_canvas_style(c1)
        c1.Divide(1, 1)
        c1.cd(1)

        h_data = RooAbsData.createHistogram(data_set, 'm_Kppim,m_pKmpip', m_Kppim, RooFit.Binning(40), RooFit.YVar(m_pKmpip, RooFit.Binning(40)))
        xtitle = 'M(K^{+}#pi^{-}) (GeV/c^{2})'
        ytitle = 'M(pK^{-}#pi^{+}) (GeV/c^{2})'
        format_data_hist(h_data)
        name_axis(h_data, xtitle, ytitle)
        h_data.Draw()

        c1.SaveAs('./figs/data_m_Kppim_m_pKmpip.pdf')

        c2 = TCanvas('c2', 'c2', 1000, 700)
        set_canvas_style(c2)
        c2.Divide(1, 1)
        c2.cd(1)

        h_2D = model.createHistogram('m_Kppim,m_pKmpip', 40, 40)
        scale = entries_data / h_2D.Integral()
        h_2D.Scale(scale)
        format_data_hist(h_2D)
        gStyle.SetPadRightMargin(0.13)
        name_axis(h_2D, xtitle, ytitle)
        h_2D.Draw('colz')

        c2.SaveAs('./figs/fit_m_Kppim_m_pKmpip.pdf')

        c3 = TCanvas('c3', 'c3', 1000, 700)
        set_canvas_style(c3)
        c3.Divide(1, 1)
        c3.cd(1)

        chi2_sum = 0
        h_chi2 = TH2F('h_chi2', 'h_chi2', 40, xmin, xmax, 40, ymin, ymax)
        format_data_hist(h_chi2)
        name_axis(h_chi2, xtitle, ytitle)
        for x in range(41):
            for y in range(41):
                nd = h_data.GetBinContent(x, y)
                nf = h_2D.GetBinContent(x, y)
                if nd == 0 or nf == 0: chi2 = 0
                else: chi2 = pow((nd - nf) / sqrt(nd), 2)
                if chi2 > 18: chi2 /= 5
                h_chi2.SetBinContent(x, y, chi2)
                chi2_sum += chi2

        h_chi2.Draw('colz')
        n_param = results.floatParsFinal().getSize()
        print(chi2_sum, 40 * 40 - n_param - 1, chi2_sum / (40 * 40 - n_param - 1))
        chi2_ndf = '#chi^{2}/ndf = ' + str(round(chi2_sum / (40 * 40 - n_param - 1), 2))
        pt_chi2 = set_pavetext(0.68, 0.8, 0.78, 0.85, 2, 0.05, chi2_ndf)
        pt_chi2.Draw()

        c3.SaveAs('./figs/chi2_m_Kppim_m_pKmpip.pdf')

        flag = input('Break or not?')
        if flag == 'Yes':
            break

def main():
    data = []
    data.append('./roots/RFSIG_RunPeriod-2018-08_ver10_upl.root')
    sig_path = './roots/DLambdac_RunPeriod-2018-08_ver10_upl.root'
    fit(data, sig_path)

if __name__ == '__main__':
    main()
