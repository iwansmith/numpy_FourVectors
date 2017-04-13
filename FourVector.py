
import numpy as np
import math

from ThreeVector import ThreeVector
	

class FourVector():
	"""
	This class tries to replicate the TLorentzVector using numpy to make everything faster
	
	Input Data should be a structured numpy array of format:
	
	X_PE, X_PX, X_PY, X_PZ
	
	"""

	
	def __init__(self, InputData = np.zeros((1,4), dtype=[('PE', np.float), ('PX', np.float), ('PY', np.float), ('PZ', np.float)] ) ):
		try:
			data = InputData.copy().view(( InputData.dtype[0], len(InputData.dtype.names) ))
		except:
				try:
					data = InputData.copy()
				except:
					nev = InputData[0].shape[0]
					data = np.concatenate( (np.reshape(InputData[0], (nev,1)), np.reshape(InputData[1], (nev,1)), np.reshape(InputData[2], (nev,1)), np.reshape(InputData[3], (nev,1))), axis = 1 )
			
		self.PE = data[:,0]
		self.fP = ThreeVector(data[:,1:4])
		
			
	def SetXYZM(self, XYZ, M):
		
		self.fP.SetXYZ( XYZ )
		self.PE = np.sqrt( self.fP.P2() + np.square( M ) )
		
		
	def SetX(self, X ):
		self.fP.SetX(X)
	def SetY(self, Y ):
		self.fP.SetY(Y)
	def SetZ(self, Z ):
		self.fP.SetZ(Z)

	
	def PX( self ):
		return self.fP.PX
	
	def PY( self ):
		return self.fP.PY
	
	def PZ( self ):
		return self.fP.PZ
	
	def __add__ ( self, vector2):
		New4V = FourVector()
		New4V.PE = self.PE + vector2.PE
		New4V.fP = self.fP + vector2.fP
		
		return New4V
	def __neg__ ( self, vector2):
		New4V = FourVector()
		New4V.PE = self.PE - vector2.PE
		New4V.fP = self.fP - vector2.fP
		
		return New4V
	def __sub__ ( self, vector2):
		New4V = FourVector()
		New4V.PE = self.PE - vector2.PE
		New4V.fP = self.fP - vector2.fP
		
		return New4V
		
	def __mul__( self, Vector2 ):
		
		return np.multiply(self.PE, Vector2.PE) - self.fP * Vector2.fP
		
	def __getitem__(self, index):
		New4V = FourVector()
		New4V.PE = self.PE[index]
		New4V.fP = self.fP[index]
		return New4V

	def __len__( self ):
		return self.PE.shape[0]
		
		
		
	def Vect(self):
		return self.fP
	def Boost( self, BetaX = 0, BetaY = 0, BetaZ = 0 ):
		
		GammaX = 1/math.sqrt( 1 - BetaX * BetaX )
		GammaY = 1/math.sqrt( 1 - BetaY * BetaY )
		GammaZ = 1/math.sqrt( 1 - BetaZ * BetaZ )
		
		newPE = GammaX * self.PE - BetaX * GammaX * self.fP.PX
		newPX = -BetaX * GammaX * self.PE + GammaX * self.fP.PX
		self.PE = newPE
		self.fP.PX = newPX
				
		newPE = GammaY * self.PE - BetaY * GammaY * self.fP.PY
		newPY = -BetaY * GammaY * self.PE + GammaY * self.fP.PY
		self.PE = newPE
		self.fP.PY = newPY
		
		newPE = GammaZ * self.PE - BetaZ * GammaZ * self.fP.PZ
		newPZ = -BetaZ * GammaZ * self.PE + GammaZ * self.fP.PZ
		self.PE = newPE
		self.fP.PZ = newPZ
		

	def M2(self):
		
		return np.square( self.PE ) - self.fP.P2()

	def M(self):
		return np.sqrt( self.M2(  ) )
	
	def P2(self):
		return self.fP.P2()

	def P(self):
		return self.fP.P()
	
	def Pt(self):
		return self.fP.Pt()

	def Perp2(self, Vector2):
		return self.fP.Perp2( Vector2 )
	
	def Perp(self, Vector2):
		return self.fP.Perp( Vector2 )
	
	def Angle(self, Vector2):
		try:
			return self.fP.Angle(Vector2.fP)
		except:
			return self.fP.Angle(Vector2)
	
	def Dot( self, V2 ):
		return self.PE * V2.PE - self.fP.PX * V2.fP.PX - self.fP.PY * V2.fP.PY - self.fP.PZ * V2.fP.PZ
