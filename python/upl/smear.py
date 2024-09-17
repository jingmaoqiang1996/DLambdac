#!/usr/bin/env python
"""
Smear likelihood distribution according to systematic uncertainty
"""

__author__ = "Maoqiang JING <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) Maoqiang JING"
__created__ = "[2020-12-03 Thu 20:42]"

import math
from array import array
from ROOT import *
import sys, os
import logging
from math import *
sys.path.append('../')
from tools import set_pub_style, set_prelim_style, set_graph_style, set_pavetext, name_axis, set_canvas_style, set_yzero_hist, set_legend, format_mc_hist, Lum, Br
import random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def usage():
    sys.stdout.write('''
NAME
    smear.py

SYNOPSIS
    ./smear.py [sample] [mode] [patch]

AUTHOR
    Maoqiang JING <jingmq@ihep.ac.cn>

DATE
    December 2020
\n''')

set_pub_style()
set_prelim_style()

def find_sys():
    path = '../sys_err/total/txts/sys_total.txt'
    with open(path) as f:
        for line in f.readlines():
            fargs = list(map(float, line.strip().split()))
            return fargs[0] / 100

def smear(path):
    try:
        f = open(path, 'r')
    except:
        logging.error(path + ' is invalid!')
        sys.exit()

    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.cd()

    with open('./txts/num_m_Kppim_m_pKmpip_fit.txt', 'r') as f:
        lines = f.readlines()
        fargs = list(map(float, lines[0].strip().split()))
        eff   = fargs[2]

    factor = 1. / (Lum() * Br('D0')[0] * Br('Lambdac')[0] * eff)

    # xtitle = 'Cross Section (pb)'
    xtitle = '#sigma_{#gammap#rightarrow#bar{D}^{0}#Lambda_{c}^{+}} (nb)'
    ytitle = 'Normalized likelihood'

    with open(path, 'r') as f:
        lines = f.readlines()
        N = len(lines) - 1
        n_set = array('f', N*[0])
        likelihood = array('f', N*[0])
        count = 0
        for i in range(N):
            fargs = list(map(float, lines[i].strip('\n').strip().split()))
            n_set[i] = fargs[0] * factor / 1000
            likelihood[i] = fargs[1]
            count += 1
    
    gr = TGraph(N, n_set, likelihood)
    set_graph_style(gr, xtitle, ytitle)

    n_smear = 5000
    a = array('f', N*[0])

    sys_err = find_sys()
    print('Systematic uncertainty is {0}'.format(sys_err))

    h_smear = TH1D('h_smear', 'h_smear', N, 0, max(n_set))
    format_mc_hist(h_smear, 17)
    name_axis(h_smear, xtitle, ytitle)

    bin_w = max(n_set) / N / 2
    for nbin, nn in enumerate(n_set):
        nevt = int(n_smear*likelihood[nbin])
        numevt = 0
        while numevt < nevt:
            bin_num = random.gauss(nn, nn * sys_err)
            numevt += 1
            if bin_num < 0: continue
            h_smear.Fill(bin_num)
    h_smear.Scale(1. / h_smear.GetMaximum())

    for i in range(N):
        prob = h_smear.Integral(0, i) / h_smear.Integral()
        if prob >= 0.9:
            pos_90 = h_smear.GetBinCenter(i)
            break
    
    h_smear.Draw('hist')
    # gr.Draw('same')

    arrow = TArrow(pos_90 * (1 + sys_err), 0.5, pos_90 * (1 + sys_err), 0., 0.02)
    arrow.SetLineStyle(1)
    arrow.SetLineColor(kRed)
    arrow.SetFillColor(kRed)
    arrow.SetLineWidth(3)
    arrow.Draw()

    pt_upl = '90% C.L.: {}'.format(round(pos_90 * (1 + sys_err), 2))
    pt = set_pavetext(0.6, 0.8, 0.7, 0.85, 1, 0.04, pt_upl)
    pt.Draw()

    if not os.path.exists('./txts/'):
        os.makedirs('./txts/')

    with open('./txts/upl_smeared.txt', 'w') as f:
        f.write(str(pos_90 * (1 + sys_err)) + '\n')

    if not os.path.exists('./figs/'):
        os.makedirs('./figs/')
    mbc.SaveAs('./figs/upper_limit_smeared.pdf')

    input('Enter anything to end...')


def main():
    path = './txts/likelihood_m_Kppim_m_pKmpip_fit_upl.txt'
    smear(path)

if __name__ == '__main__':
    main()
