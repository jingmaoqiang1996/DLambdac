#!usr/bin/env python

"""
flatte: convert root files after reaction filter to fsroot readable files
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-07-02 Tue 00:01]"

import sys
import subprocess

def usage():
    sys.stdout.write(
        '''
        NAME
            flatten_fsroot.py

        SYNOPSYS
            ./flatten_fsroot.py [input file list] [RunPeriod] [version] [analysis]

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            July 2024
        \n'''
    )

def check_result(result):
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    args = sys.argv[1:]
    if len(args) < 6:
        return usage()

    input_list  = args[0]
    run_period  = args[1]
    version     = args[2]
    analysis    = args[3]
    sample_type = args[4]
    file_idx    = args[5]

    output_dir  = '$RAWROOTDIR/' + sample_type + '/DLambdac/' + analysis
    cmd         = 'mkdir -p ' + output_dir
    result = subprocess.run(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    check_result(result)

    with open(input_list, 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip('\n')
            cmd = 'flatten -in ' + line + ' -out ' + output_dir + '/' + sample_type + '_' + run_period + '_' + version + '_' + analysis + '_' + file_idx + '_' + str(idx) + '.root '
            cmd += '-chi2 200 -massWindows 0.5 -numNeutralHypos 2 -numUnusedTracks 0 -usePolarization 1'
            result = subprocess.run(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            check_result(result)

if __name__ == '__main__':
    main()
