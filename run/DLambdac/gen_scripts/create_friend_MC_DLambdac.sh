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

mkdir -p $LOGDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    FILE="$RAWROOTDIR/mc/DLambdac/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root"
    cd $LOGDIR
    FILENAME="Create_Friend_MC_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}"
    echo "#!/usr/bin/env bash" > $FILENAME
    echo "cd $PYDIR" >> $FILENAME
    echo "python create_friend.py ${FILE}" >> $FILENAME
    chmod u+x $LOGDIR/$FILENAME
    # sbatch $LOGDIR/$FILENAME
    bash $LOGDIR/$FILENAME
    COUNT=$((${COUNT} + 1))
done
