#!/usr/bin/env python
"""
Calculate upper limit of total DDpipi cross section
"""

__author__ = "Maoqiang JING <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) Maoqiang JING"
__created__ = "[2020-12-03 Thu 21:24]"

import math
from array import array
from ROOT import *
import sys, os
import logging
from math import *
sys.path.append('../')
from tools import set_pub_style, set_prelim_style, set_graph_style, set_pavetext, name_axis, set_canvas_style, set_yzero_hist, set_legend, Lum, Br
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def usage():
    sys.stdout.write('''
NAME
    upper_limit.py

SYNOPSIS
    ./upper_limit.py [sample] [patch]

AUTHOR
    Maoqiang JING <jingmq@ihep.ac.cn>

DATE
    December 2020
\n''')

set_pub_style()
set_prelim_style()

def upper_limit(path):
    try:
        f = open(path, 'r')
    except:
        logging.error(path + ' is invalid!')
        sys.exit()

    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.SetLeftMargin(0.18)
    mbc.SetRightMargin(0.1)
    mbc.SetTopMargin(0.05)
    mbc.SetBottomMargin(0.22)
    mbc.cd()

    with open('./txts/num_m_Kppim_m_pKmpip_fit.txt', 'r') as f:
        lines = f.readlines()
        fargs = list(map(float, lines[0].strip().split()))
        eff   = fargs[2]

    factor = 1. / (Lum() * Br('D0')[0] * Br('Lambdac')[0] * eff)

    # xtitle = 'Cross Section (pb)'
    xtitle = '#sigma_{#gammap#rightarrow#bar{D}^{0}#Lambda_{c}^{+}} (nb)'
    ytitle = 'Normalized likelihood'

    FCN_sum = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        N = len(lines) - 1
        xs_set = array('f', N*[0])
        likelihood = array('f', N*[0])
        count = 0
        # for line in lines:
        for i in range(len(lines) - 1):
            fargs = list(map(float, lines[i].strip('\n').strip().split()))
            xs_set[count] = fargs[0] * factor / 1000
            likelihood[count] = fargs[1]
            if xs_set[count] < 0: continue
            FCN_sum += fargs[1]
            count += 1
    print('Number = ' + str(N))
    print('Sum of FCN: ' + str(FCN_sum))

    t = 0
    sum_90 = 0
    for i in range(N):
        if xs_set[i] < 0: continue
        if sum_90 < FCN_sum*0.9:
            sum_90 += likelihood[i]
            pos_90 = xs_set[i]
            t += 1

    nf = t + 3
    xs_set_f = array('f', nf*[0])
    likelihood_f = array('f', nf*[0])
    xs_set_f[0], likelihood_f[0] = 0, 0
    xs_set_f[nf - 2], likelihood_f[nf - 2] = pos_90, 0
    xs_set_f[nf - 1], likelihood_f[nf - 1] = 0, 0

    j = 0
    sumf_90 = 0
    for i in range(N):
        if xs_set[i] < 0: continue
        if sumf_90 < FCN_sum*0.9:
            j += 1
            sumf_90 += likelihood[i]
            likelihood_f[j] = likelihood[i]
            xs_set_f[j] = xs_set[i]
            print('xs(setted): ' + str(xs_set_f[j]) + ', likelihood: ' + str(likelihood_f[j]))

    print('90% C.L. = ' + str(pos_90) + ', the 90% of FCN sum = ' + str(sum_90))

    xs_set_max = -9999
    likelihood_max = 0
    for i in range(N):
        if xs_set[i] < 0: continue
        if likelihood_max < likelihood[i]:
            likelihood_max = likelihood[i]
            xs_set_max = xs_set[i]

    print('The maximum of likelihood = ' + str(likelihood_max) + ', cross section = ' + str(xs_set_max))

    gr = TGraph(N, xs_set, likelihood)
    set_graph_style(gr, xtitle, ytitle)
    gr.Draw('APC')

    gf = TGraph(nf, xs_set_f, likelihood_f)
    gf.SetFillColor(40)
    gf.Draw('LF')

    arrow = TArrow(pos_90, likelihood_max*0.5, pos_90, 0., 0.02)
    arrow.SetLineStyle(1)
    arrow.SetLineColor(kRed)
    arrow.SetFillColor(kRed)
    arrow.SetLineWidth(3)
    arrow.Draw()

    pt_upl = '90% C.L.: {}'.format(round(pos_90, 2))
    pt = set_pavetext(0.45, 0.65, 0.65, 0.85, 1, 0.04, pt_upl)
    pt.Draw()

    # if not os.path.exists('./txts/'):
    #     os.makedirs('./txts/')
    # with open('./txts/upl_'+str(sample)+'.txt', 'w') as f:
    #     f.write(str(sample)+' '+str(round(pos_90, 2)))

    if not os.path.exists('./figs/'):
        os.makedirs('./figs/')
    mbc.SaveAs('./figs/upper_limit.pdf')

    input('Enter anything to end...')

def main():
    path = './txts/likelihood_m_Kppim_m_pKmpip_fit_upl.txt'
    upper_limit(path)

if __name__ == '__main__':
    main()
