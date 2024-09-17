#/bin/bash

# RUNS=(
# "RunPeriod-2018-08"
# "RunPeriod-2018-08"
# "RunPeriod-2018-08"
# )
# VERS=(
# "ver10"
# "ver10"
# "ver10"
# )
# ANAS=(
# "DLambdac"
# "ppippimKpKm"
# "ppippimpippim"
# )
# TREES=(
# "ntFSGlueX_100_110110"
# "ntFSGlueX_100_110110"
# "ntFSGlueX_100_110110"
# )

RUNS=(
"RunPeriod-2018-08"
"RunPeriod-2018-08"
)
VERS=(
"ver10"
"ver10"
)
ANAS=(
"DLambdac"
"DLambdac_PHSP"
)
TREES=(
"ntFSGlueX_100_110110"
"ntFSGlueX_100_110110"
)

COUNT=0
mkdir -p $ANAROOTDIR
for RUN in ${RUNS[@]}; do
    mkdir -p $ANAROOTDIR/mc/DLambdac/${ANAS[$COUNT]}
    FILE="$RAWROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root"
    cd $LOGDIR
    FILENAME="Apply_Cuts_MC_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}"
    echo "#!/usr/bin/env bash" > $FILENAME
    echo "$FSROOT/Executables/FSSkimTree -i \"${FILE}\" -o \"$ANAROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/FIT_RFSIG_${RUN}_${VERS[$COUNT]}_100_110110.root\" -cuts \"((EnPB>8.7)&&(Chi2<55)&&(ProdVz >= 52 && ProdVz <= 78)&&(NumUnusedTracks == 0)&&(abs(RFDeltaT)<2.0)&&(MASS(1,3,4)>2.2&&MASS(1,3,4)<2.35)&&(MASS(2,5)>1.7&&MASS(2,5)<2.0)&&(MASS(2,3)>1.05)&&(!(MASS(1,3)>1.5&&MASS(1,3)<1.54))&&(MASS(1,4)>1.33))\" -nt \"${TREES[$COUNT]}\" -friend \"Chi2Rank\"" >> $FILENAME
    chmod u+x $LOGDIR/$FILENAME
    sbatch $LOGDIR/$FILENAME
    COUNT=$((${COUNT} + 1))
done
