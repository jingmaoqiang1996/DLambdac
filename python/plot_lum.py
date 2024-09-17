#!usr/bin/env python
import ROOT, sys, os
from ROOT import TCanvas, TGaxis, TFile
sys.path.append('../')
from tools import set_canvas_style, set_pub_style, set_prelim_style, format_data_hist, name_axis, set_legend, format_mc_hist
set_pub_style()
set_prelim_style()
TGaxis.SetMaxDigits(3)

"""
distribution: draw luminosity
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-09-07 Sat 17:23]"

def usage():
    sys.stdout.write(
        '''
        NAME
            plot_lum.py

        SYNOPSYS
            ./plot_lum.py

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            September 2024
        \n'''
    )

def draw():
    f_in = TFile('$ANAROOTDIR/data/DLambdac/flux_50685_51768_600_bins.root')
    h_lum = f_in.Get('tagged_lumi')

    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.SetTopMargin(0.08)
    mbc.SetRightMargin(0.05)
    mbc.cd()

    xtitle = 'E_{beam} (GeV)'
    ytitle = 'Luminosity (pb^{-1})'
    format_mc_hist(h_lum, 1)
    name_axis(h_lum, xtitle, ytitle)

    h_lum.Draw('hist')

    if not os.path.exists('./figs/'): os.makedirs('./figs/')
    mbc.SaveAs('./figs/lum.pdf')

    input('Press <Enter> to end ...')

def main():
    draw()

if __name__ == '__main__':
    main()
