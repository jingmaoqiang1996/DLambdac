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

COUNT=0
mkdir -p $ANAROOTDIR
for RUN in ${RUNS[@]}; do
    mkdir -p $ANAROOTDIR/bggen/DLambdac
    FILE="$RAWROOTDIR/bggen/DLambdac/bggen_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root"
    cd $LOGDIR
    FILENAME="Skim_BgGen_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}"
    echo "#!/usr/bin/env bash" > $FILENAME
    echo "$FSROOT/Executables/FSSkimTree -i \"${FILE}\" -o \"$ANAROOTDIR/bggen/DLambdac/SKIM_RFSIG_${RUN}_${VERS[$COUNT]}_100_110110.root\" -cuts \"((Chi2DOF<200.0)&&(abs(RFDeltaT)<2.0)&&(MASS(1,3,4)>2.2&&MASS(1,3,4)<2.35)&&(MASS(2,5)>1.7&&MASS(2,5)<2.0))\" -nt \"${TREES[$COUNT]}\" -friend \"Chi2Rank\"" >> $FILENAME
    chmod u+x $LOGDIR/$FILENAME
    sbatch $LOGDIR/$FILENAME
    COUNT=$((${COUNT} + 1))
done
