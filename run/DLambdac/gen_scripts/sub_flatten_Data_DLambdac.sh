#/bin/bash

RUNS=(
"RunPeriod-2018-01"
)
VERS=(
"ver13"
)
ANAS=(
"tree_pippimkpkm__B4"
)

mkdir -p $LOGDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    FILES="$WORKDIR/run/DLambdac/samples/data/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/"
    IDX=0
    find "$FILES" -type f | while read FILE; do
	cd $WORKDIR/run/DLambdac/gen_scripts
        FILENAME="Flatten_Data_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_${IDX}"
        echo "#!/usr/bin/env bash" > $FILENAME
        echo "cd $PYDIR" >> $FILENAME
        echo "python flatten_fsroot.py $FILE $RUN ${VERS[$COUNT]} ${ANAS[$COUNT]} data $IDX" >> $FILENAME
        mv $WORKDIR/run/DLambdac/gen_scripts/$FILENAME $LOGDIR/$FILENAME
	cd $LOGDIR
        chmod u+x $LOGDIR/$FILENAME
        sbatch $LOGDIR/$FILENAME
        IDX=$((${IDX} + 1))
    done
    COUNT=$((${COUNT} + 1))
done
