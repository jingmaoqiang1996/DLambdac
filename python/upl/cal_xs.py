#!usr/bin/env python
import ROOT, sys, os
from array import array
sys.path.append('../')
from tools import Lum, Br

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

def cal_xs():
    br = Br('D0')[0] * Br('Lambdac')[0]
    
    if not os.path.exists('./txts/'):
        os.makedirs('./txts/')

    with open('./txts/num_m_Kppim_m_pKmpip_fit.txt', 'r') as f:
        lines = f.readlines()
        fargs = list(map(float, lines[0].strip().split()))
        N     = fargs[0]
        N_err = fargs[1]
        eff   = fargs[2]
    
    sigma = N / (Lum() * br * eff)
    sigma_err = N_err / (Lum() * br * eff)

    with open('./txts/xs_mean.txt', 'w') as f:
        f.write(str(sigma / 1000.) + ' ' + str(sigma_err / 1000.))

def main():
    cal_xs()

if __name__ == '__main__':
    main()
