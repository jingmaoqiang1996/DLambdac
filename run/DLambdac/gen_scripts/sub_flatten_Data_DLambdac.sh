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

COUNT=0
for RUN in ${RUNS[@]}; do
    FILES="$WORKDIR/run/DLambdac/samples/data/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/"
    IDX=0
    find "$FILES" -type f | while read FILE; do
        FILENAME="Flatten_Data_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_${IDX}"
        echo "#!/usr/bin/env bash" > $FILENAME
        echo "cd $PYDIR" >> $FILENAME
        echo "python flatten_fsroot.py $FILE $RUN ${VERS[$COUNT]} ${ANAS[$COUNT]} data $IDX" >> $FILENAME
        mkdir -p $WORKDIR/run/DLambdac/log_files
        mv $WORKDIR/run/DLambdac/gen_scripts/$FILENAME $WORKDIR/run/DLambdac/log_files/$FILENAME
        chmod u+x $WORKDIR/run/DLambdac/log_files/$FILENAME
        # sbatch $WORKDIR/run/DLambdac/log_files/$FILENAME
        IDX=$((${IDX} + 1))
    done
    COUNT=$((${COUNT} + 1))
done
