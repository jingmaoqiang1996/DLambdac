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
event selection: scatter DEDXCDC v.s. P
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-08-14 Wed 18:42]"

def usage():
    sys.stdout.write(
        '''
        NAME
            scatter_DEDXCDC_P.py

        SYNOPSYS
            ./scatter_DEDXCDC_P.py

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            August 2024
        \n'''
    )

def get_hist(path, tree_name, xmin, xmax, xbins, ymin, ymax, ybins):
    FSTree.addFriendTree('Chi2Rank')
    cut_rank = '(Chi2RankGlobal == 1)'
    cut_EnPB = '(EnPB > 8.7)'
    cut_Vz = '(ProdVz >= 52 && ProdVz <= 78)'
    cut_Chi2DOF = '(Chi2 < 55)'
    cut_NUMTRK = '(NumUnusedTracks == 0)'
    cut_range_Lambdac = '(MASS([p+], [K+], [pi-]) > 2.2 && MASS([p+], [K+], [pi-]) < 2.35)'
    cut_range_D       = '(MASS([K-], [pi+]) > 1.7 && MASS([K-], [pi+]) < 2.0)'
    cut_phi_1020      = '(MASS([K+], [K-]) > 1.05)'
    cut_Lambda_1520   = '!(MASS([p+], [K-]) > 1.5 && MASS([p+], [K-]) < 1.54)'
    cut_Delta_1235    = '(MASS([p+], [pi+]) > 1.33)'
    FSCut.defineCut('rank', cut_rank)
    FSCut.defineCut('EnPB', cut_EnPB)
    FSCut.defineCut('Vz', cut_Vz)
    FSCut.defineCut('Chi2DOF', cut_Chi2DOF)
    FSCut.defineCut('NUMTRK', cut_NUMTRK)
    FSCut.defineCut('range_Lambdac', cut_range_Lambdac)
    FSCut.defineCut('range_D', cut_range_D)
    FSCut.defineCut('phi_1020', cut_phi_1020)
    FSCut.defineCut('Lambda_1520', cut_Lambda_1520)
    FSCut.defineCut('Delta_1235', cut_Delta_1235)
    # h = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[K-]*1000000:MOMENTUM([K-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h_Kp = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[K+]*1000000:MOMENTUM([K+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h_pip = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[pi+]*1000000:MOMENTUM([pi+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h_pim = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[pi-]*1000000:MOMENTUM([pi-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h_p = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[p+]*1000000:MOMENTUM([p+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h.Add(h_Kp)
    # h.Add(h_pip)
    # h.Add(h_pim)
    # h.Add(h_p)
    # xtitle = 'p (GeV/#it{c})'
    # ytitle = 'CDC dE/dx (keV/cm)'
    # format_data_hist(h)
    # name_axis(h, xtitle, ytitle)
    # return h
    # # kaon
    # h = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[K-]*1000000:MOMENTUM([K-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h_Kp = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[K+]*1000000:MOMENTUM([K+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # h.Add(h_Kp)
    # xtitle = 'p (GeV/#it{c})'
    # ytitle = 'CDC dE/dx (keV/cm)'
    # format_data_hist(h)
    # name_axis(h, xtitle, ytitle)
    # return h
    # pion
    h = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[pi-]*1000000:MOMENTUM([pi-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    h_pip = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[pi+]*1000000:MOMENTUM([pi+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    h.Add(h_pip)
    xtitle = 'p (GeV/#it{c})'
    ytitle = 'CDC dE/dx (keV/cm)'
    format_data_hist(h)
    name_axis(h, xtitle, ytitle)
    return h
    # # proton
    # h = FSModeHistogram.getTH2F(path, tree_name, '', 'TkDEDXCDCP[p+]*1000000:MOMENTUM([p+])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ', ' + str(ybins) + ', ' + str(ymin) + ', ' + str(ymax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    # xtitle = 'p (GeV/#it{c})'
    # ytitle = 'CDC dE/dx (keV/cm)'
    # format_data_hist(h)
    # name_axis(h, xtitle, ytitle)
    # return h

def draw(run_periods, versions, xmin, xmax, xbins, ymin, ymax, ybins, mode):
    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.cd()

    tree_name = 'ntFSGlueX_MODECODE'
    FSModeCollection.addModeInfo('p+ K+ K- pi+ pi-')

    hist_mg = {}
    for run_period, version in zip(run_periods, versions):
        if mode == 'data': path = '$ANAROOTDIR/data/DLambdac/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        else: path = '$ANAROOTDIR/mc/DLambdac/' + mode + '/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        hist_mg['h_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, ymin, ymax, ybins)

    max = 0
    for key in hist_mg.keys():
        hist_mg[key].Draw('colz')

    f_exp1 = TF1('f_exp', 'exp(-4. * x + 2.25) + 1.0', xmin, xmax)
    f_exp1.SetLineColor(2)
    f_exp1.Draw('same')

    f_exp2 = TF1('f_exp', 'exp(-7. * x + 3.0) + 6.2', xmin, xmax)
    f_exp2.SetLineColor(3)
    f_exp2.Draw('same')

    # f_exp = TF1('f_exp', 'exp(-2.5 * x + 2.5) + 1.0', xmin, xmax)
    # f_exp.Draw('same')

    # f_0 = TF1('f_0', 'exp(-22.0 * x + 3.0) + 1.4', xmin, xmax)
    # f_0.SetLineColor(1)
    # f_0.Draw('same')

    # f_1 = TF1('f_1', 'exp(-7.0 * x + 3.0) + 1.4', xmin, xmax)
    # f_1.SetLineColor(2)
    # f_1.Draw('same')

    # f_2 = TF1('f_2', 'exp(-4.0 * x + 3.0) + 1.4', xmin, xmax)
    # f_2.SetLineColor(3)
    # f_2.Draw('same')

    # f_4 = TF1('f_4', 'exp(-2.0 * x + 3.0) + 1.4', xmin, xmax)
    # f_4.SetLineColor(5)
    # f_4.Draw('same')

    if not os.path.exists('./figs/'): os.makedirs('./figs/')
    mbc.SaveAs('./figs/scatter_DEDXCDC_P_' + mode + '_pion.pdf')

    input('Press <Enter> to end ...')

def main():
    args = sys.argv[1:]
    if len(args)<1:
        return usage()
    mode = args[0]

    run_periods = ['RunPeriod-2018-08']
    versions    = ['ver10']
    xmin, xmax, xbins = 0., 3., 50
    ymin, ymax, ybins = 0.2, 10., 50
    draw(run_periods, versions, xmin, xmax, xbins, ymin, ymax, ybins, mode)

if __name__ == '__main__':
    main()
