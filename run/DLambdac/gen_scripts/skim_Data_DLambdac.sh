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

COUNT=0
mkdir -p $ANAROOTDIR
for RUN in ${RUNS[@]}; do
    mkdir -p $ANAROOTDIR/data/DLambdac
    FILE="$RAWROOTDIR/data/DLambdac/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root"
    cd $LOGDIR
    FILENAME="Skim_Data_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}"
    echo "#!/usr/bin/env bash" > $FILENAME
    echo "$FSROOT/Executables/FSSkimTree -i \"${FILE}\" -o \"$ANAROOTDIR/data/DLambdac/SKIM_RFSIG_${RUN}_${VERS[$COUNT]}_100_110110.root\" -cuts \"((EnPB>8.7)&&(Chi2<200)&&(abs(RFDeltaT)<2.0)&&(MASS(1,3,4)>2.2&&MASS(1,3,4)<2.35)&&(MASS(2,5)>1.7&&MASS(2,5)<2.0))\" -nt \"ntFSGlueX_100_110110\" -friend \"Chi2Rank\"" >> $FILENAME
    echo "$FSROOT/Executables/FSSkimTree -i \"${FILE}\" -o \"$ANAROOTDIR/data/DLambdac/SKIM_RFSB_${RUN}_${VERS[$COUNT]}_100_110110.root\" -cuts \"((EnPB>8.7)&&(Chi2<200)&&(abs(RFDeltaT)>2.0&&abs(RFDeltaT)<6.0)&&(MASS(1,3,4)>2.2&&MASS(1,3,4)<2.35)&&(MASS(2,5)>1.7&&MASS(2,5)<2.0))\" -nt \"ntFSGlueX_100_110110\" -friend \"Chi2Rank\"" >> $FILENAME
    chmod u+x $LOGDIR/$FILENAME
    sbatch $LOGDIR/$FILENAME
    COUNT=$((${COUNT} + 1))
done