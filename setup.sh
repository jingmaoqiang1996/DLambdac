export WORKDIR=$PWD
export PYDIR=$PWD/python
export ANAROOTDIR=/P/stan/data/maojing/DLambdac/run/DLambdac/anaroot
source /P/stan/data/shared/ROOT/6.30.02/bin/thisroot.sh
export PATH=/P/stan/data/maojing/software/hd_utilities/FlattenForFSRoot:$PATH
export FSROOT="/P/stan/data/maojing/software/FSRoot"
export DYLD_LIBRARY_PATH="${DYLD_LIBRARY_PATH}:${FSROOT}"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${FSROOT}"
