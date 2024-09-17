#!usr/bin/env python
import ROOT, sys, os
ROOT.gSystem.Load('$FSROOT/FSBasic/FSTree_C.so')
ROOT.gSystem.Load('$FSROOT/FSBasic/FSCut_C.so')
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeHistogram_C.so')
from ROOT import TCanvas, FSTree, FSCut, TGaxis, FSModeCollection, FSModeHistogram, THStack
sys.path.append('../')
from tools import set_canvas_style, set_pub_style, set_prelim_style, format_data_hist, name_axis, set_legend, format_mc_hist
set_pub_style()
set_prelim_style()
TGaxis.SetMaxDigits(3)

"""
event selection: draw M(K-pi+pi-)
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-07-17 Wed 17:05]"

def usage():
    sys.stdout.write(
        '''
        NAME
            plot_m_Kmpippim.py

        SYNOPSYS
            ./plot_m_Kmpippim.py

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            July 2024
        \n'''
    )

def get_hist(path, tree_name, xmin, xmax, xbins, color):
    FSTree.addFriendTree('Chi2Rank')
    cut_rank = 'Chi2RankGlobal == 1'
    cut_EnPB = 'EnPB > 8.7'
    cut_Vz = 'ProdVz >= 52 && ProdVz <= 78'
    cut_Chi2DOF = 'Chi2 < 55'
    cut_NUMTRK = 'NumUnusedTracks == 0'
    cut_range_Lambdac = 'MASS([p+], [K-], [pi+]) > 2.2 && MASS([p+], [K-], [pi+]) < 2.35'
    cut_range_D       = 'MASS([K+], [pi-]) > 1.7 && MASS([K+], [pi-]) < 2.0'
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
    h_data = FSModeHistogram.getTH1F(path, tree_name, '', 'MASS([K-], [pi+], [pi-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    xtitle = 'M(K^{-}#pi^{+}#pi^{-}) (MeV/#it{c}^{2})'
    content = int((xmax - xmin)/xbins * 1000)
    ytitle = 'Events/%.1f MeV/#it{c}^{2}'%content
    if color == -1: format_data_hist(h_data)
    else: format_mc_hist(h_data, color)
    name_axis(h_data, xtitle, ytitle)
    return h_data

def get_hist_ws(path, tree_name, xmin, xmax, xbins, color):
    FSTree.addFriendTree('Chi2Rank')
    cut_rank = 'Chi2RankGlobal == 1'
    cut_EnPB = 'EnPB > 8.7'
    cut_Vz = 'ProdVz >= 52 && ProdVz <= 78'
    cut_Chi2DOF = 'Chi2 < 55'
    cut_NUMTRK = 'NumUnusedTracks == 0'
    cut_range_Lambdac = 'MASS([p+], [K+], [pi-]) > 2.2 && MASS([p+], [K+], [pi-]) < 2.35'
    cut_range_D       = 'MASS([K-], [pi+]) > 1.7 && MASS([K-], [pi+]) < 2.0'
    cut_phi_1020      = '(MASS([K+], [K-]) > 1.05)'
    cut_Lambda_1520   = '!(MASS([p+], [K+]) > 1.5 && MASS([p+], [K+]) < 1.54)'
    cut_Delta_1235    = '(MASS([p+], [pi-]) > 1.33)'
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
    h_data = FSModeHistogram.getTH1F(path, tree_name, '', 'MASS([K+], [pi+], [pi-])', '(' + str(xbins) + ', ' + str(xmin) + ', ' + str(xmax) + ')', 'CUT(rank, EnPB, Vz, Chi2DOF, NUMTRK, range_Lambdac, range_D, phi_1020, Lambda_1520, Delta_1235)')
    xtitle = 'M(K^{-}#pi^{+}#pi^{-}) (MeV/#it{c}^{2})'
    content = int((xmax - xmin)/xbins * 1000)
    ytitle = 'Events/%.1f MeV/#it{c}^{2}'%content
    if color == -1: format_data_hist(h_data)
    else: format_mc_hist(h_data, color)
    name_axis(h_data, xtitle, ytitle)
    return h_data

def draw(run_periods, versions, xmin, xmax, xbins):
    mbc = TCanvas('mbc', 'mbc', 800, 600)
    set_canvas_style(mbc)
    mbc.SetTopMargin(0.08)
    mbc.SetRightMargin(0.05)
    mbc.cd()

    tree_name = 'ntFSGlueX_MODECODE'
    FSModeCollection.addModeInfo('p+ K+ K- pi+ pi-')
    data_hist_mg, side_hist_mg, mc_hist_mg, p2K2pi_hist_mg, p4pi_hist_mg, ws_hist_mg = {}, {}, {}, {}, {}, {}
    for run_period, version in zip(run_periods, versions):
        path = '$ANAROOTDIR/data/DLambdac/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        data_hist_mg['h_data_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, -1)
        path = '$ANAROOTDIR/data/DLambdac/SKIM_RFSB_' + run_period + '_' + version + '_MODECODE.root'
        side_hist_mg['h_side_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, 3)
        path = '$ANAROOTDIR/mc/DLambdac/DLambdac_PHSP/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        mc_hist_mg['h_mc_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, 2)
        path = '$ANAROOTDIR/mc/DLambdac/ppippimKpKm/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        p2K2pi_hist_mg['h_2K2pi_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, 4)
        path = '$ANAROOTDIR/mc/DLambdac/ppippimpippim/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE.root'
        p4pi_hist_mg['h_4pi_' + run_period + '_' + version] = get_hist(path, tree_name, xmin, xmax, xbins, 7)
        path = '$ANAROOTDIR/data/DLambdac/SKIM_RFSIG_' + run_period + '_' + version + '_MODECODE_wrong_sign.root'
        ws_hist_mg['h_ws_' + run_period + '_' + version] = get_hist_ws(path, tree_name, xmin, xmax, xbins, 3)

    max = 0
    for data_key, side_key, mc_key, p2K2pi_key, p4pi_key, ws_key in zip(data_hist_mg.keys(), side_hist_mg.keys(), mc_hist_mg.keys(), p2K2pi_hist_mg.keys(), p4pi_hist_mg.keys(), ws_hist_mg.keys()):
        data_hist_mg[data_key].Draw('same')
        ws_hist_mg[ws_key].SetFillStyle(0)
        ws_hist_mg[ws_key].Draw('samehist')
        hs = THStack('hs', 'Stacked')
        p4pi_hist_mg[p4pi_key].Scale(1.2 * 2)
        p2K2pi_hist_mg[p2K2pi_key].Scale(2.0 * 2)
        p2K2pi_hist_mg[p2K2pi_key].Scale(1/5.)
        mc_hist_mg[mc_key].Scale(0.00070192776)
        hs.Add(p2K2pi_hist_mg[p2K2pi_key])
        hs.Add(p4pi_hist_mg[p4pi_key])
        hs.Add(mc_hist_mg[mc_key])
        hs.Draw('samehist')
        side_hist_mg[side_key].Scale(0.5)
        side_hist_mg[side_key].Draw('samehist')
        data_hist_mg[data_key].Draw('same')
        if data_hist_mg[data_key].GetMaximum() > max:
            max = data_hist_mg[data_key].GetMaximum()

    legend = set_legend(
            [data_hist_mg[data_key], ws_hist_mg[ws_key], side_hist_mg[side_key], p2K2pi_hist_mg[p2K2pi_key], p4pi_hist_mg[p4pi_key], mc_hist_mg[mc_key]],
            ['data', 'WS background', 'RF #DeltaT sideband', '#gammap#rightarrowK^{-}K^{+}#pi^{+}#pi^{-}', '#gammap#rightarrow#pi^{-}#pi^{+}#pi^{+}#pi^{-}', '#gammap#rightarrowD^{0}#Lambda_{c}^{+}'],
            ['lep', 'f', 'f', 'f', 'f', 'f'],
            0.7, 0.7, 0.9, 0.9, 2
    )
    legend.Draw()

    if not os.path.exists('./figs/'): os.makedirs('./figs/')
    mbc.SaveAs('./figs/m_Kmpippim.pdf')

    input('Press <Enter> to end ...')

def main():
    run_periods = ['RunPeriod-2018-08']
    versions    = ['ver10']
    xmin, xmax = 0.8, 3.2
    xbins = int(abs(xmax - xmin)/0.01)
    draw(run_periods, versions, xmin, xmax, xbins)

if __name__ == '__main__':
    main()
