#!usr/bin/env python
import ROOT, sys, os
ROOT.gSystem.Load('$FSROOT/FSBasic/FSTree_C.so')
ROOT.gSystem.Load('$FSROOT/FSBasic/FSCut_C.so')
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeHistogram_C.so')
from ROOT import TCanvas, FSTree, FSCut, TGaxis, FSModeCollection, FSModeHistogram, TF1
sys.path.append('../')
from tools import set_canvas_style, set_pub_style, set_prelim_style, format_data_hist, name_axis, set_legend, format_mc_hist
set_pub_style()
set_prelim_style()
TGaxis.SetMaxDigits(3)

"""
event selection: draw M(K-pi+)
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-07-16 Mon 15:59]"

def usage():
    sys.stdout.write(
        '''
        NAME
            plot_m_Kmpip.py

        SYNOPSYS
            ./plot_m_Kmpip.py

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            July 2024
        \n'''
    )

def get_hist(path, tree_name, xmin, xmax, xbins, ymin, ymax, ybins):
    FSTree.addFriendTree('Chi2Rank')
    cut_rank = 'Chi2RankGlobal == 1'
    cut_Vz = 'ProdVz >= 52 && ProdVz <= 78'
    cut_Chi2DOF = 'Chi2 < 55'
    cut_NUMTRK = 'NumUnusedTracks == 0'
    cut_range_Lambdac = 'MASS([p+], [K+], [pi-]) > 2.2 && MASS([p+], [K+], [pi-]) < 2.35'
    cut_range_D       = 'MASS([K-], [pi+]) > 1.7 && MASS([K-], [pi+]) < 2.0'
    cut_rho_770       = '!(MASS([pi+], [pi-]) > 0.545 && MASS([pi+], [pi-]) < 0.995)'
    cut_phi_1020      = '(MASS([K+], [K-]) > 1.05)'
    cut_N_star        = '(MASS([p+], [pi+], [pi-]) > 1.9)'
    cut_Lambda_1520   = '!(MASS([p+], [K-]) > 1.5 && MASS([p+], [K-]) < 1.54)'
    FSCut.defineCut('rank', cut_rank)
    FSCut.defineCut('Vz', cut_Vz)
    FSCut.defineCut('Chi2DOF', cut_Chi2DOF)
    FSCut.defineCut('NUMTRK', cut_NUMTRK)
    FSCut.defineCut('range_Lambdac', cut_range_Lambdac)
    FSCut.defineCut('range_D', cut_range_D)
    FSCut.defineCut('rho_770', cut_rho_770)
    FSCut.defineCut('phi_1020', cut_phi_1020)
    FSCut.defineCut('N_star', cut_N_star)
    FSCut.defineCut('Lambda_1520', cut_Lambda_1520)
    h_data = FSModeHistogram.getTH2F(path, tree_name, '', 'MASS([K-], [pi+]):MASS([p+], [K+], [pi-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, rho_770, phi_1020, N_star, Lambda_1520)')
    xtitle = 'M(pK^{+}#pi^{-}) (MeV/#it{c}^{2})'
    ytitle = 'M(K^{-}#pi^{+}) (MeV/#it{c}^{2})'
    format_data_hist(h_data)
    name_axis(h_data, xtitle, ytitle)
    return h_data

def draw(run_periods, versions, xmin, xmax, xbins, ymin, ymax, ybins, mode):
    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.cd()

    tree_name = 'ntFSGlueX_MODECODE'
    FSModeCollection.addModeInfo('p+ K+ K- pi+ pi-')

    data_hist_mg = {}
    for run_period, version in zip(run_periods, versions):
        if mode == 'data': path = '$ANAROOTDIR/data/DLambdac/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        if mode == 'mc': path = '$ANAROOTDIR/mc/DLambdac/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        data_hist_mg['h_data_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, ymin, ymax, ybins)

    for data_key in data_hist_mg.keys():
        data_hist_mg[data_key].Draw('colz')

    if not os.path.exists('./figs/'): os.makedirs('./figs/')
    mbc.SaveAs('./figs/scatter_m_Kmpip_m_pKppim_' + mode + '.pdf')

    input('Press <Enter> to end ...')

def main():
    args = sys.argv[1:]
    if len(args)<1:
        return usage()
    mode = args[0]

    run_periods = ['RunPeriod-2018-08']
    versions    = ['ver10']
    xmin, xmax, xbins = 2.2, 2.35, 20
    ymin, ymax, ybins = 1.7, 2.0, 20
    draw(run_periods, versions, xmin, xmax, xbins, ymin, ymax, ybins, mode)

if __name__ == '__main__':
    main()
