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
SOURCES=(
"/P/stan/scratch/GlueX/RunPeriod-2018-08/analysis/ver10/tree_pippimkpkm__T1_S2/merged/"
)

FILENAME="Gen_FileList_Data_DLambdac"
echo "#!/usr/bin/env bash" > $FILENAME
echo "cd $WORKDIR" >> $FILENAME
COUNT=0
for RUN in ${RUNS[@]}; do
    echo "rm -r $WORKDIR/run/DLambdac/samples/data/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/*txt" >> $FILENAME
    echo "./python/get_samples.py ${SOURCES[$COUNT]} ./run/DLambdac/samples/data/$RUN/${VERS[$COUNT]}/${ANAS[$COUNT]}/data_${RUN}_${VERS[$COUNT]}_${ANAS[$COUNT]}_DLambdac.txt 3G" >> $FILENAME
    COUNT=$((${COUNT} + 1))
done

mkdir -p $WORKDIR/run/DLambdac/log_files
mv $WORKDIR/run/DLambdac/gen_scripts/Gen_FileList_Data_DLambdac $WORKDIR/run/DLambdac/log_files/Gen_FileList_Data_DLambdac
cd $WORKDIR/run/DLambdac/log_files/
bash Gen_FileList_Data_DLambdac
