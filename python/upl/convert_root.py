#!usr/bin/env python
import ROOT, sys, os
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
from ROOT import TCanvas, TLorentzVector, TFile, TTree, FSModeInfo
from array import array
sys.path.append('../')
from tools import format_data_hist, name_axis, format_mc_hist

"""
convert root files
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-08-27 Tue 18:50]"

def usage():
    sys.stdout.write(
        '''
        NAME
            convert_root.py

        SYNOPSYS
            ./convert_root.py

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            August 2024
        \n'''
    )

def convert(path, tree_name, run_period, version, type):
    f_in = TFile(path)
    t_in = f_in.Get(tree_name)
    t_in.AddFriend(tree_name + '_Chi2Rank', path + '.Chi2Rank')
    f_out = TFile('./roots/' + type + '_' + run_period + '_' + version + '_upl.root', 'recreate')
    t_out = TTree(tree_name, tree_name)
    m_m_Kppim  = array('d', [999.])
    m_m_pKmpip = array('d', [999.])
    t_out.Branch('m_Kppim',  m_m_Kppim,  'm_m_Kppim/D')
    t_out.Branch('m_pKmpip', m_m_pKmpip, 'm_m_pKmpip/D')

    for idx, evt in enumerate(t_in):
        if not (evt.Chi2RankGlobal == 1): continue
        if idx%1000 == 0: print('Processing {}/{} events...'.format(idx, evt.GetEntries()))
        pp   = TLorentzVector(t_in.PxP1, t_in.PyP1, t_in.PzP1, t_in.EnP1)
        pKp  = TLorentzVector(t_in.PxP2, t_in.PyP2, t_in.PzP2, t_in.EnP2)
        pKm  = TLorentzVector(t_in.PxP3, t_in.PyP3, t_in.PzP3, t_in.EnP3)
        ppip = TLorentzVector(t_in.PxP4, t_in.PyP4, t_in.PzP4, t_in.EnP4)
        ppim = TLorentzVector(t_in.PxP5, t_in.PyP5, t_in.PzP5, t_in.EnP5)
        m_m_Kppim[0]  = (pKp + ppim).M()
        m_m_pKmpip[0] = (pp + pKm + ppip).M()
        t_out.Fill()

    f_out.cd()
    t_out.Write()
    f_out.Close()

def draw(run_periods, versions):
    mi = FSModeInfo('p+ K+ K- pi+ pi-')
    mc = str(mi.modeString())
    tree_name = 'ntFSGlueX_MODECODE'.replace('MODECODE', mc)

    if not os.path.exists('./roots/'): os.makedirs('./roots/')
    for run_period, version in zip(run_periods, versions):
        path = '$ANAROOTDIR/data/DLambdac/FIT_RFSIG_' + run_period + '_' + version + '_' + mc + '.root'
        convert(path, tree_name, run_period, version, 'RFSIG')
        path = '$ANAROOTDIR/mc/DLambdac/DLambdac_PHSP/FIT_RFSIG_' + run_period + '_' + version + '_' + mc + '.root'
        convert(path, tree_name, run_period, version, 'DLambdac')

def main():
    run_periods = ['RunPeriod-2018-08']
    versions    = ['ver10']
    draw(run_periods, versions)

if __name__ == '__main__':
    main()
