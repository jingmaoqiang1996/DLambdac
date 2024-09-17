#!usr/bin/env python
import sys, os
from math import *

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

def cal():
    # sys_err = ['bkg', 'Delta_1235', 'Kst_892', 'E_beam', 'Lambda_1520', 'chi2', 'phi_1020', 'br']
    sys_err = ['br']
    if not os.path.exists('./txts/'):
        os.makedirs('./txts/')

    dic_sys = {}
    with open('./txts/sys_err.txt', 'w') as f_out:
        for s in sys_err:
            with open('../' + s + '/txts/xs_diff.txt') as f:
                lines = f.readlines()
                diff1 = float(lines[0].strip().split()[0])
            f_out.write(s + ' ' + str(diff1) + '\n')
            dic_sys.update({s: diff1})
    sum_sys = 0
    for k, v in dic_sys.items():
        sum_sys += v * v

    with open('./txts/sys_total.txt', 'w') as f:
        f.write(str(sqrt(sum_sys)))

def main():
    cal()

if __name__ == '__main__':
    main()
