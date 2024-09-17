#!usr/bin/env python
import ROOT, sys, os
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
from ROOT import TCanvas, TLorentzVector, TFile, TTree, FSModeInfo
from array import array

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
    m_E_beam   = array('d', [999.])
    m_chi2     = array('d', [999.])
    m_m_Kppim  = array('d', [999.])
    m_m_KpKm   = array('d', [999.])
    m_m_pKm    = array('d', [999.])
    m_m_ppip   = array('d', [999.])
    m_m_pKmpip = array('d', [999.])
    t_out.Branch('E_beam',   m_E_beam,   'm_E_beam/D')
    t_out.Branch('chi2',     m_chi2,     'm_chi2/D')
    t_out.Branch('m_Kppim',  m_m_Kppim,  'm_m_Kppim/D')
    t_out.Branch('m_KpKm',   m_m_KpKm,   'm_m_KpKm/D')
    t_out.Branch('m_pKm',    m_m_pKm,    'm_m_pKm/D')
    t_out.Branch('m_ppip',   m_m_ppip,   'm_m_ppip/D')
    t_out.Branch('m_pKmpip', m_m_pKmpip, 'm_m_pKmpip/D')

    for idx, evt in enumerate(t_in):
        if not (evt.Chi2RankGlobal == 1): continue
        if idx%1000 == 0: print('Processing {}/{} events...'.format(idx, evt.GetEntries()))
        pp   = TLorentzVector(t_in.PxP1, t_in.PyP1, t_in.PzP1, t_in.EnP1)
        pKp  = TLorentzVector(t_in.PxP2, t_in.PyP2, t_in.PzP2, t_in.EnP2)
        pKm  = TLorentzVector(t_in.PxP3, t_in.PyP3, t_in.PzP3, t_in.EnP3)
        ppip = TLorentzVector(t_in.PxP4, t_in.PyP4, t_in.PzP4, t_in.EnP4)
        ppim = TLorentzVector(t_in.PxP5, t_in.PyP5, t_in.PzP5, t_in.EnP5)
        m_E_beam[0]   = t_in.EnPB
        m_chi2[0]     = t_in.Chi2
        m_m_Kppim[0]  = (pKp + ppim).M()
        m_m_KpKm[0]   = (pKp + pKm).M()
        m_m_pKm[0]    = (pp + pKm).M()
        m_m_ppip[0]   = (pp + ppip).M()
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
        path = '$ANAROOTDIR/mc/DLambdac/DLambdac/FIT_RFSIG_' + run_period + '_' + version + '_' + mc + '.root'
        convert(path, tree_name, run_period, version, 'DLambdac')

def main():
    run_periods = ['RunPeriod-2018-08']
    versions    = ['ver10']
    draw(run_periods, versions)

if __name__ == '__main__':
    main()
