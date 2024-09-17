#/bin/bash

RUNS=(
"RunPeriod-2018-08"
)
VERS=(
"ver01"
)
ANAS=(
"pippimkpkm"
)
TREES=(
"ntFSGlueX_100_110110"
)

mkdir -p $RAWROOTDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    cd $PYDIR
    rm -rf $RAWROOTDIR/bggen/DLambdac/bggen_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root
    python merge.py ${TREES[$COUNT]} $RAWROOTDIR/bggen/DLambdac/bggen_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root $RAWROOTDIR/bggen/DLambdac/bggen_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_*.root 
    COUNT=$((${COUNT} + 1))
done
