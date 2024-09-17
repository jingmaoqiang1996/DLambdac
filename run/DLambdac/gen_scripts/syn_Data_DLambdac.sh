#/bin/bash

RUNS=(
"RunPeriod-2018-08"
)
VERS=(
"ver10"
)
ANAS=(
"tree_pippimkpkm__T1_S2"
)
TREES=(
"ntFSGlueX_100_110110"
)

mkdir -p $RAWROOTDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    cd $PYDIR
    rm -rf $RAWROOTDIR/data/DLambdac/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root
    python merge.py ${TREES[$COUNT]} $RAWROOTDIR/data/DLambdac/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root $RAWROOTDIR/data/DLambdac/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_*.root 
    COUNT=$((${COUNT} + 1))
done
