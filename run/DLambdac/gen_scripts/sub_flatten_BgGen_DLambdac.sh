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

mkdir -p $LOGDIR
COUNT=0
for RUN in ${RUNS[@]}; do
    FILES="$WORKDIR/run/DLambdac/samples/bggen/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/"
    IDX=0
    find "$FILES" -type f | while read FILE; do
	cd $WORKDIR/run/DLambdac/gen_scripts
        FILENAME="Flatten_BgGen_DLambdac_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_${IDX}"
        echo "#!/usr/bin/env bash" > $FILENAME
        echo "cd $PYDIR" >> $FILENAME
        echo "python flatten_fsroot.py $FILE $RUN ${VERS[$COUNT]} ${ANAS[$COUNT]} bggen $IDX" >> $FILENAME
        mv $WORKDIR/run/DLambdac/gen_scripts/$FILENAME $LOGDIR/$FILENAME
	cd $LOGDIR
        chmod u+x $LOGDIR/$FILENAME
        sbatch $LOGDIR/$FILENAME
        IDX=$((${IDX} + 1))
    done
    COUNT=$((${COUNT} + 1))
done
