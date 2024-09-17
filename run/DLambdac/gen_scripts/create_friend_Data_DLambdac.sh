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


mkdir -p $LOGDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    FILE="$RAWROOTDIR/data/DLambdac/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}.root"
    cd $LOGDIR
    FILENAME="Create_Friend_Data_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}"
    echo "#!/usr/bin/env bash" > $FILENAME
    echo "cd $PYDIR" >> $FILENAME
    echo "python create_friend.py ${FILE}" >> $FILENAME
    chmod u+x $LOGDIR/$FILENAME
    # sbatch $LOGDIR/$FILENAME
    bash $LOGDIR/$FILENAME
    COUNT=$((${COUNT} + 1))
done
