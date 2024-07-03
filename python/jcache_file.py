#!usr/bin/env python

"""
jache: force data samples to disk
"""

__author__    = "JING Maoqiang <jingmq@ihep.ac.cn>"
__copyright__ = "Copyright (c) JING Maoqiang"
__created__   = "[2024-07-01 Mon 23:13]"


import sys
import subprocess

def usage():
    sys.stdout.write(
        '''
        NAME
            jcache_file.py

        SYNOPSYS
            ./jcache_file.py [RunPeriod] [version] [analysis]

        AUTHOR
            JING Maoqiang <jingmq@ihep.ac.cn>

        DATE
            July 2024
        \n'''
    )

def main():
    args = sys.argv[1:]
    if len(args) < 3:
        return usage()

    RunPeriod = args[0]
    version   = args[1]
    analysis  = args[2]

    cmd = 'jcache get /mss/halld/' + RunPeriod + '/analysis/' + version + '/' + analysis + '/merged/*'
    result = subprocess.run(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == '__main__':
    main()