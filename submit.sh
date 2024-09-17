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
    printf "\n\t%-9s  %-40s"  "0.2"       "[run on mc sample]"
    printf "\n\n"
}

usage_0_1() {
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n\t%-9s  %-40s"  "0.1.1"     "Force data samples to the disk [do this in JLab server]"
    printf "\n\t%-9s  %-40s"  "0.1.2"     "Split data samples into group of files"
    printf "\n\t%-9s  %-40s"  "0.1.3"     "Submit jobs for data samples"
    printf "\n\t%-9s  %-40s"  "0.1.4"     "Synthesize data samples"
    printf "\n\t%-9s  %-40s"  "0.1.5"     "Create friend tree"
    printf "\n\t%-9s  %-40s"  "0.1.6"     "Skim data samples"
    printf "\n\t%-9s  %-40s"  "0.1.7"     "Apply cuts on data samples"
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n"
}

usage_0_2() {
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n\t%-9s  %-40s"  "0.2.1"     "Split mc samples into group of files"
    printf "\n\t%-9s  %-40s"  "0.2.2"     "Submit jobs for mc samples"
    printf "\n\t%-9s  %-40s"  "0.2.3"     "Synthesize mc samples"
    printf "\n\t%-9s  %-40s"  "0.2.4"     "Create friend tree"
    printf "\n\t%-9s  %-40s"  "0.2.5"     "Skim mc samples"
    printf "\n\t%-9s  %-40s"  "0.2.6"     "Apply cuts on mc samples"
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n"
}

usage_0_3() {
    printf "\n\t%-9s  %-40s"  ""          ""
    printf "\n\t%-9s  %-40s"  "0.3.1"     "Split bggen samples into group of files"
    printf "\n\t%-9s  %-40s"  "0.3.2"     "Submit jobs for mc samples"
    printf "\n\t%-9s  %-40s"  "0.3.3"     "Synthesize bggen samples"
    printf "\n\t%-9s  %-40s"  "0.3.4"     "Create friend tree"
    printf "\n\t%-9s  %-40s"  "0.3.5"     "Skim mc samples"
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
        python jcache_file.py RunPeriod-2018-08 ver10 tree_pippimkpkm__T1_S2 # T1: one extra trak, S2: 2 extra showers
    ;;

    0.1.2) echo "Split data samples into group of files ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./make_file_list_Data_DLambdac.sh
    ;;

    0.1.3) echo "Submit jobs for data samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./sub_flatten_Data_DLambdac.sh
    ;;

    0.1.4) echo "Synthesize data samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./syn_Data_DLambdac.sh
    ;;

    0.1.5) echo "Create friend tree ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./create_friend_Data_DLambdac.sh
    ;;

    0.1.6) echo "Skim data samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./skim_Data_DLambdac.sh
    ;;

    0.1.7) echo "Apply cuts on data samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./apply_cut_Data_DLambdac.sh
    ;;

esac

}


sub_0_2() {

case $option in

    # --------------------------------------------------------------------------
    #  run on mc sample
    # --------------------------------------------------------------------------

    0.2.1) echo "Split mc samples into group of files ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./make_file_list_MC_DLambdac.sh
    ;;

    0.2.2) echo "Submit jobs for mc samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./sub_flatten_MC_DLambdac.sh
    ;;

    0.2.3) echo "Synthesize mc samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./syn_MC_DLambdac.sh
    ;;

    0.2.4) echo "Create friend tree ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./create_friend_MC_DLambdac.sh
    ;;

    0.2.5) echo "Skim mc samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./skim_MC_DLambdac.sh
    ;;

    0.2.6) echo "Apply cuts on mc samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./apply_cut_MC_DLambdac.sh
    ;;

esac

}


sub_0_3() {

case $option in

    # --------------------------------------------------------------------------
    #  run on mc sample
    # --------------------------------------------------------------------------

    0.3.1) echo "Split bggen samples into group of files ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./make_file_list_BgGen_DLambdac.sh
    ;;

    0.3.2) echo "Submit jobs for bggen samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./sub_flatten_BgGen_DLambdac.sh
    ;;

    0.3.3) echo "Synthesize mc samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./syn_BgGen_DLambdac.sh
    ;;

    0.3.4) echo "Create friend tree ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./create_friend_BgGen_DLambdac.sh
    ;;

    0.3.5) echo "Skim bggen samples ..."
        cd $WORKDIR/run/DLambdac/gen_scripts/
        ./skim_BgGen_DLambdac.sh
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

    # --------------------------------------------------------------------------
    #  MC
    # --------------------------------------------------------------------------

    0.2) echo "Running on mc sample ..."
        usage_0_2
        echo "Please enter your option: "
        read option
        sub_0_2 option
    ;;

    0.2.*) echo "Running on mc sample ..."
        sub_0_2 option
    ;;

    # --------------------------------------------------------------------------
    #  BgGen
    # --------------------------------------------------------------------------

    0.3) echo "Running on bggen sample ..."
        usage_0_3
        echo "Please enter your option: "
        read option
        sub_0_3 option
    ;;

    0.3.*) echo "Running on bggen sample ..."
        sub_0_3 option
    ;;

esac
