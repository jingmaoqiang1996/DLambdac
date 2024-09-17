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
SOURCES=(
"/P/stan/scratch/maojing/DLambdac/run/DLambdac/reactionfilter/RunPeriod-2018-08/analysis/ver01/batch01/tree_pippimkpkm/merged/"
)

FILENAME="Gen_FileList_BgGen_DLambdac"
echo "#!/usr/bin/env bash" > $FILENAME
echo "cd $WORKDIR" >> $FILENAME
COUNT=0
for RUN in ${RUNS[@]}; do
    echo "rm -r $WORKDIR/run/DLambdac/samples/bggen/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/*txt" >> $FILENAME
    echo "./python/get_samples.py ${SOURCES[$COUNT]} ./run/DLambdac/samples/bggen/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/BgGen_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_DLambdac.txt 1G" >> $FILENAME
    COUNT=$((${COUNT} + 1))
done

mkdir -p $WORKDIR/run/DLambdac/log_files
mv $WORKDIR/run/DLambdac/gen_scripts/Gen_FileList_BgGen_DLambdac $WORKDIR/run/DLambdac/log_files/Gen_FileList_BgGen_DLambdac
cd $WORKDIR/run/DLambdac/log_files/
bash Gen_FileList_BgGen_DLambdac
