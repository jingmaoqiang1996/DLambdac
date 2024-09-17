#!usr/bin/env python
"""
create friend trees after reaction filter to fsroot readable files
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-07-19 Thu 12:02]"

import sys, ROOT
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeTree_C.so')
from ROOT import FSModeTree
from tools import get_name

def usage():
    sys.stdout.write(
        '''
        NAME
            create_friend.py

        SYNOPSYS
            ./create_friend.py [input file]

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            July 2024
        \n'''
    )

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        return usage()

    input_file  = args[0]

    nt_name, _ = get_name()
    tree_name = 'ntFSGlueX_' + str(nt_name)
    FSModeTree.createChi2RankingTree(input_file, str(tree_name), '', '')

if __name__ == '__main__':
    main()
