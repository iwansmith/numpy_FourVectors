import sys
sys.path.append('../')


from FourVector import FourVector

import numpy as np
import ROOT
from root_numpy import root2array


branches_Kp = ["Kplus_TRUEP_E",  "Kplus_TRUEP_X",  "Kplus_TRUEP_Y",  "Kplus_TRUEP_Z" ]
branches_Km = ["Kminus_TRUEP_E", "Kminus_TRUEP_X", "Kminus_TRUEP_Y", "Kminus_TRUEP_Z" ]


NumpyData = root2array("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsMuNu/MCDecayTree",
	branches = branches_Kp + branches_Km
)

K_p = FourVector( NumpyData[branches_Kp] )
K_m = FourVector( NumpyData[branches_Km] )
Phi = K_p + K_m

nev = len(Phi)


h_Phi = ROOT.TH1F("h_Phi", "#Phi invariant mass", 1000, 1000, 1040)
h_Phi.FillN( nev, Phi.M(), np.ones( nev ) ) 

c1 = ROOT.TCanvas("c1", "c1", 900, 900)
h_Phi.Draw()
c1.Print( "Example.pdf" )
