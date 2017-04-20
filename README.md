# Three Vector and Four Vector implementation using numpy

This attempts to replicate TLorentzVector and TVector3 from ROOT using numpy.

Please note that this is a work in progress, so not all functions have been transfered over.



The most basic usage is very similar to TLorentzVector:

```
In [1]: from FourVector import FourVector

In [2]: # Generate Two Kaons

In [3]: #Use the standard TLorentzVector Constructor

In [4]: Kplus  = FourVector(3567.06, -2206.11, 54175.99, 54340.33904788)

In [5]: # Use SetXYZM()

In [6]: Kminus = FourVector()

In [7]: Kminus.SetXYZM(3398.82, -633.59, 49368.01, 493.677)

In [8]: # Build a Phi Candidate:

In [9]: Phi = Kplus + Kminus

In [10]: print Phi.M()
1755.09049972
```

This constrcutors can take lists and numpy arrays in addition to floats.
