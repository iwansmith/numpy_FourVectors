import sys
sys.path.append('../')


from FourVector import FourVector

import numpy as np
import ROOT
from root_numpy import root2array, tree2array


branches_Ds = ["Ds_PE",  "Ds_PX",  "Ds_PY",  "Ds_PZ" ]
branches_Pi = ["muon_p_PX", "muon_p_PY", "muon_p_PZ" ]


Chain = ROOT.TChain("Bs2DsMuNuTuple/DecayTree")
print Chain.Add("root://eoslhcb.cern.ch//eos/lhcb/wg/semileptonic/Bs2KmunuAna/Tuples/Bs2DsMuNu_DATATUPLES_RAW_19June16/*_DTT_*_SEMILEPTONIC.root")

NumpyData = tree2array(Chain,
	branches = branches_Ds + branches_Pi
)


#Fill the Ds using the standard constructor
Ds = FourVector( NumpyData[branches_Ds] )

#We want to change the mass hypothesis of the muon so initialise an empty FourVector and use SetXYZM.
Pi = FourVector(  )
Pi.SetXYZM( NumpyData[branches_Pi], 139.57, Debug=True )

#print Pi.PE, Pi.PX(), Pi.PY(), Pi.PZ(), Ds.PE
Bs = Ds + Pi

nev = len(Bs)


h_Bs = ROOT.TH1F("h_Bs", "#D_{s} + #pi invariant mass", 100, 5000, 6000)
h_Bs.FillN( nev, Bs.M(), np.ones( nev ) ) 

c1 = ROOT.TCanvas("c1", "c1", 900, 900)
h_Bs.Draw()
c1.Print( "Example_Bs.pdf" )
