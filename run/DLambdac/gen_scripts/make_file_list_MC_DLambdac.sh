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
SOURCES=(
"/P/stan/scratch/maojing/DLambdac/run/DLambdac/reactionfilter/RunPeriod-2018-08/analysis/ver10/DLambdac/"
"/P/stan/scratch/maojing/DLambdac/run/DLambdac/reactionfilter/RunPeriod-2018-08/analysis/ver10/DLambdac_PHSP/"
"/P/stan/scratch/maojing/DLambdac/run/DLambdac/reactionfilter/RunPeriod-2018-08/analysis/ver10/ppippimKpKm/"
"/P/stan/scratch/maojing/DLambdac/run/DLambdac/reactionfilter/RunPeriod-2018-08/analysis/ver10/ppippimpippim/"
)

FILENAME="Gen_FileList_MC_DLambdac"
echo "#!/usr/bin/env bash" > $FILENAME
echo "cd $WORKDIR" >> $FILENAME
COUNT=0
for RUN in ${RUNS[@]}; do
    echo "rm -r $WORKDIR/run/DLambdac/samples/mc/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/*txt" >> $FILENAME
    echo "./python/get_samples.py ${SOURCES[$COUNT]} ./run/DLambdac/samples/mc/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/mc_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_DLambdac.txt 1G" >> $FILENAME
    COUNT=$((${COUNT} + 1))
done

mkdir -p $WORKDIR/run/DLambdac/log_files
mv $WORKDIR/run/DLambdac/gen_scripts/Gen_FileList_MC_DLambdac $WORKDIR/run/DLambdac/log_files/Gen_FileList_MC_DLambdac
cd $WORKDIR/run/DLambdac/log_files/
bash Gen_FileList_MC_DLambdac
