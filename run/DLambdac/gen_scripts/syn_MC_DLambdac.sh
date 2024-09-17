#/bin/bash

RUNS=(
"RunPeriod-2018-08"
"RunPeriod-2018-08"
"RunPeriod-2018-08"
"RunPeriod-2018-08"
)
VERS=(
"ver10"
"ver10"
"ver10"
"ver10"
)
ANAS=(
"DLambdac"
"DLambdac_PHSP"
"ppippimKpKm"
"ppippimpippim"
)
TREES=(
"ntFSGlueX_100_110110"
"ntFSGlueX_100_110110"
"ntFSGlueX_100_110110"
"ntFSGlueX_100_110110"
)

mkdir -p $RAWROOTDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    cd $PYDIR
    rm -rf $RAWROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root
    python merge.py ${TREES[$COUNT]} $RAWROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root $RAWROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_*.root 
    COUNT=$((${COUNT} + 1))
done
