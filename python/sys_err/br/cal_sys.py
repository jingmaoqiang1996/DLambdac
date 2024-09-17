#!usr/bin/env python
import sys, os
from math import *
sys.path.append('../../')
from tools import Br

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
    if not os.path.exists('./txts/'):
        os.makedirs('./txts/')

    with open('./txts/xs_diff.txt', 'w') as f:
        D0_sys = Br('D0')[1] / Br('D0')[0] * 100
        Lambdac_sys = Br('Lambdac')[1] / Br('Lambdac')[0] * 100
        f.write(str(sqrt(D0_sys ** 2 + Lambdac_sys ** 2)))

def main():
    cal()

if __name__ == '__main__':
    main()
