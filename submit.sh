#!/usr/bin/env bash

# Main driver to submit jobs
# Author JING Maoqiang <jingmq@ihep.ac.cn>
# Created [2024-07-01 Mon 23:42]

usage() {
    printf "NAME\n\tsubmit.sh - Main driver to submit jobs\n"
    printf "\nSYNOPSIS\n"
    printf "\n\t%-5s\n" "./submit.sh [OPTION]"
    printf "\nOPTIONS\n"
    printf "\n\t%-9s  %-40s"  "0.1"       "[run on data sample]"
    printf "\n\n"
}

usage_0_1() {
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n\t%-9s  %-40s"  "0.1.1"     "Force data samples to the disk [do this in JLab server]"
    printf "\n\t%-9s  %-40s"  "0.1.2"     "Split data samples into group of files"
    printf "\n\t%-9s  %-40s"  "0.1.3"     "Submit jobs for data samples"
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n"
}

if [[ $# -eq 0 ]]; then
    usage
    echo "Please enter your option: "
    read option
else
    option=$1
fi

sub_0_1() {

case $option in

    # --------------------------------------------------------------------------
    #  run on data sample
    # --------------------------------------------------------------------------

    0.1.1) echo "Force data samples to the disk [do this in JLab server] ..."
        cd $WORKDIR/python/
        python jcache_file.py RunPeriod-2018-01 ver13 tree_pippimkpkm__B4
    ;;

    0.1.2) echo "Split data samples into group of files ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./make_file_list_Data_DLambdac.sh
    ;;

    0.1.3) echo "Submit jobs for data samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./sub_flatten_Data_DLambdac.sh
    ;;

esac

}


case $option in

    # --------------------------------------------------------------------------
    #  Data
    # --------------------------------------------------------------------------

    0.1) echo "Running on data sample ..."
        usage_0_1
        echo "Please enter your option: "
        read option
        sub_0_1 option
    ;;

    0.1.*) echo "Running on data sample ..."
        sub_0_1 option
    ;;

esac
