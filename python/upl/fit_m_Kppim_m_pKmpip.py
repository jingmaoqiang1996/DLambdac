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

        xframe = m_Kppim.frame(RooFit.Bins(xbins), RooFit.Range(xmin, xmax))
        xtitle = 'M(K^{+}#pi^{-}) (GeV/c^{2})'
        content = (xmax - xmin)/xbins * 1000
        ytitle = 'Entries/%.1f MeV'%content
        format_data_hist(xframe)
        name_axis(xframe, xtitle, ytitle)
        data_set.plotOn(xframe, RooFit.Name('data_m_Kppim'))
        model.plotOn(xframe, RooFit.LineColor(kBlue), RooFit.Name('pdf_total_m_Kppim'))
        sig_list = ['sigpdf_m_Kppim_sigpdf_m_pKmpip']
        bkg_list = ['sigpdf_m_Kppim_bkgpdf_m_pKmpip', 'bkgpdf_m_Kppim_sigpdf_m_pKmpip', 'bkgpdf_m_Kppim_bkgpdf_m_pKmpip']
        colors = [2, 3, 4, 6]
        lines  = [1, 10, 10, 10]
        n_comp = [
                    'S_{M(K^{-}#pi^{+})}#timesS_{M(pK^{+}#pi^{-})}',
                    'S_{M(K^{-}#pi^{+})}#timesB_{M(pK^{+}#pi^{-})}',
                    'B_{M(K^{-}#pi^{+})}#timesS_{M(pK^{+}#pi^{-})}',
                    'B_{M(K^{-}#pi^{+})}#timesB_{M(pK^{+}#pi^{-})}',
                ]
        h_comp, s_comp = [], []
        for idx, comp in enumerate(sig_list):
            model.plotOn(xframe, RooFit.Components(comp), RooFit.LineStyle(colors[idx]), RooFit.LineColor(colors[idx]), RooFit.Name(comp + '_m_Kppim'))
            h_comp.append(comp + '_m_Kppim')
            s_comp.append('l')
        for idx, comp in enumerate(bkg_list):
            model.plotOn(xframe, RooFit.Components(comp), RooFit.LineStyle(colors[idx + 1]), RooFit.LineColor(colors[idx + 1]), RooFit.Name(comp + '_m_Kppim'))
            h_comp.append(comp + '_m_Kppim')
            s_comp.append('l')
        data_set.plotOn(xframe, RooFit.Name('data_m_Kppim'))
        xframe.GetYaxis().SetRangeUser(0, 1.1 * xframe.GetMaximum())
        xframe.Draw()

        legend_comp = set_legend(h_comp, n_comp, s_comp, 0.68, 0.65, 0.78, 0.85, 2, size = 0.05)
        legend_comp.Draw()

        c1.SaveAs('./figs/fit_m_Kppim.pdf')

        c2 = TCanvas('c2', 'c2', 1000, 700)
        set_canvas_style(c2)
        c2.Divide(1, 1)
        c2.cd(1)

        yframe = m_pKmpip.frame(RooFit.Bins(ybins), RooFit.Range(ymin, ymax))
        xtitle = 'M(pK^{-}#pi^{+}) (GeV/c^{2})'
        content = (ymax - ymin)/ybins * 1000
        ytitle = 'Entries/%.1f MeV'%content
        format_data_hist(yframe)
        name_axis(yframe, xtitle, ytitle)
        data_set.plotOn(yframe, RooFit.Name('data_m_pKmpip'))
        model.plotOn(yframe, RooFit.LineColor(kBlue), RooFit.Name('pdf_total_m_pKmpip'))
        sig_list = ['sigpdf_m_Kppim_sigpdf_m_pKmpip']
        bkg_list = ['sigpdf_m_Kppim_bkgpdf_m_pKmpip', 'bkgpdf_m_Kppim_sigpdf_m_pKmpip', 'bkgpdf_m_Kppim_bkgpdf_m_pKmpip']
        colors = [2, 3, 4, 6]
        lines  = [1, 10, 10, 10]
        n_comp = [
                    'S_{M(K^{-}#pi^{+})}#timesS_{M(pK^{+}#pi^{-})}',
                    'S_{M(K^{-}#pi^{+})}#timesB_{M(pK^{+}#pi^{-})}',
                    'B_{M(K^{-}#pi^{+})}#timesS_{M(pK^{+}#pi^{-})}',
                    'B_{M(K^{-}#pi^{+})}#timesB_{M(pK^{+}#pi^{-})}',
                ]
        h_comp, s_comp = [], []
        for idx, comp in enumerate(sig_list):
            model.plotOn(yframe, RooFit.Components(comp), RooFit.LineStyle(colors[idx]), RooFit.LineColor(colors[idx]), RooFit.Name(comp + '_m_pKmpip'))
            h_comp.append(comp + '_m_pKmpip')
            s_comp.append('l')
        for idx, comp in enumerate(bkg_list):
            model.plotOn(yframe, RooFit.Components(comp), RooFit.LineStyle(colors[idx + 1]), RooFit.LineColor(colors[idx + 1]), RooFit.Name(comp + '_m_pKmpip'))
            h_comp.append(comp + '_m_pKmpip')
            s_comp.append('l')
        data_set.plotOn(yframe, RooFit.Name('data_m_pKmpip'))
        yframe.GetYaxis().SetRangeUser(0, 1.1 * yframe.GetMaximum())
        yframe.Draw()

        legend_comp = set_legend(h_comp, n_comp, s_comp, 0.68, 0.25, 0.78, 0.45, 2, size = 0.05)
        legend_comp.Draw()

        c2.SaveAs('./figs/fit_m_pKmpip.pdf')

        flag = input('Break or not?')
        if flag == 'Yes':
            break

    # write fit numbers
    if not os.path.exists('./txts/'):
        os.makedirs('./txts/')

    with open('./txts/num_m_Kppim_m_pKmpip_fit.txt', 'w') as f:
        f.write(str(num_sigpdf_m_Kppim_sigpdf_m_pKmpip.getVal()) + ' ' + str(num_sigpdf_m_Kppim_sigpdf_m_pKmpip.getError()) + ' ' + str(entries_sig/5000000.) + '\n')

    with open('./txts/likelihood_m_Kppim_m_pKmpip_fit.txt', 'w') as f:
        f.write(str(results.minNll()) + ' ' + str(len(results.floatParsFinal())) + '\n')

def main():
    data = []
    data.append('./roots/RFSIG_RunPeriod-2018-08_ver10_upl.root')
    sig_path = './roots/DLambdac_RunPeriod-2018-08_ver10_upl.root'
    fit(data, sig_path)

if __name__ == '__main__':
    main()
