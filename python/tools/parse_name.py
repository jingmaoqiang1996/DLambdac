import ROOT
ROOT.gSystem.Load('$FSROOT/FSMode/FSModeCollection_C.so')
from ROOT import FSModeCollection

def get_name():
    FSModeCollection.addModesFromFile('$PYDIR/modes/SigMode.modes')
    mi = FSModeCollection.modeVector('SIG')[0]
    return mi.modeString(), mi.modeGlueXName()