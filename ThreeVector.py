import numpy as np
import math


class ThreeVector:


	def __init__(self, InputData = np.zeros((1,3), dtype=[('PX', np.float), ('PY', np.float), ('PZ', np.float)] ) ):

		try:
			data = InputData.copy().view(( InputData.dtype[0], len(InputData.dtype.names) ))
		except:
				try:
					data = InputData.copy()

				except:
					nev = InputData[0].shape[0]
					data = np.concatenate( (np.reshape(InputData[0], (nev,1)), np.reshape(InputData[1], (nev,1)), np.reshape(InputData[2], (nev,1))), axis = 1 )
		
		self.PX = data[:,0]
		self.PY = data[:,1]
		self.PZ = data[:,2]
		
	def SetXYZ(self, XYZ):
		#try:
		self.PX = XYZ.PX.copy()
		self.PY = XYZ.PY.copy()
		self.PZ = XYZ.PZ.copy()
		"""
		except:
			try:
				XYZ2 = XYZ.copy().view(( XYZ.dtype[0], len(XYZ.dtype.names) ))
			except:
				XYZ2 = XYZ.copy()
				
			self.PX = XYZ2[:,0]
			self.PY = XYZ2[:,1]
			self.PZ = XYZ2[:,2]
		"""
	
	def SetX(self, X):
		try:
			self.PX = X.copy().view(( X.dtype[0], len(X.dtype.names) ))
		except:
			self.PX = X.copy()

	def SetY(self, Y):
		try:
			self.PY = Y.copy().view(( Y.dtype[0], len(Y.dtype.names) ))
		except:
			self.PY = Y.copy()

	def SetZ(self, Z):
		try:
			self.PZ = Z.copy().view(( Z.dtype[0], len(Z.dtype.names) ))
		except:
			self.PZ = Z.copy()

	
	def __add__ ( self, vector2):
		New3V = ThreeVector()
		New3V.PX = self.PX + vector2.PX
		New3V.PY = self.PY + vector2.PY
		New3V.PZ = self.PZ + vector2.PZ
		
		return New3V
	def __neg__ ( self, vector2):
		New3V = ThreeVector()
		New3V.PX = self.PX - vector2.PX
		New3V.PY = self.PY - vector2.PY
		New3V.PZ = self.PZ - vector2.PZ
		
		return New3V
		
	def __sub__ ( self, vector2):
		New3V = ThreeVector()
		New3V.PX = self.PX - vector2.PX
		New3V.PY = self.PY - vector2.PY
		New3V.PZ = self.PZ - vector2.PZ
		return New3V
		
		return New3V
		
	def __mul__( self, Vector2 ):
		try:
			return self.PX * Vector2.PX + self.PY * Vector2.PY + self.PZ * Vector2.PZ
		except:
			newThreeVector = ThreeVector()
			newThreeVector.PX = np.multiply( self.PX, Vector2 )
			newThreeVector.PY = np.multiply( self.PY, Vector2 )
			newThreeVector.PZ = np.multiply( self.PZ, Vector2 )
			return newThreeVector
	
	def __div__( self, Vector2 ):
		newThreeVector = ThreeVector()
		newThreeVector.PX = np.divide( self.PX, Vector2 )
		newThreeVector.PY = np.divide( self.PY, Vector2 )
		newThreeVector.PZ = np.divide( self.PZ, Vector2 )
		return newThreeVector
		
		
	def __getitem__( self, index ):
		newThreeVector = ThreeVector()
		newThreeVector.PX = self.PX[index]
		newThreeVector.PY = self.PY[index]
		newThreeVector.PZ = self.PZ[index]
		return newThreeVector
		
	
	def __len__( self ):
		return self.PX.shape[0]
	
	
	def P2(self):
		return np.square( self.PX) + np.square( self.PY ) + np.square( self.PZ ) 
	def P(self):
		return np.sqrt( self.P2() )
		
	def Pt(self):
		return np.sqrt( np.square( self.PX) + np.square( self.PY ) )

	def Eta(self):
		return numpy.arctanh( self.PZ / self.P() )
	
	def Mag2(self):
		return np.square(self.PX) + np.square(self.PY) + np.square(self.PZ)
		
	def Dot(self, V2):
		return self.PX * V2.PX + self.PY * V2.PY + self.PZ * V2.PZ
	
	def Perp2( self, Vector2):
		tot = Vector2.Mag2()
		ss= self.Dot(Vector2)
		per = self.Mag2()
		per -= ss*ss/tot
		return per

	def Perp( self, Vector2):
		
		return np.sqrt( self.Perp2( Vector2 ))
		
	def Angle( self, Vector2 ):
		ptot2 = self.Mag2()*Vector2.Mag2()
			
		arg = self.Dot(Vector2)/np.sqrt(ptot2)
		return np.arccos( arg )
		
		
	def Unit( self ):
		Magnitude = np.sqrt( np.square(self.PX) + np.square(self.PY) + np.square(self.PZ) )
		
		UnitVector = ThreeVector()
		UnitVector.PX = np.divide( self.PX, Magnitude)
		UnitVector.PY = np.divide( self.PY, Magnitude)
		UnitVector.PZ = np.divide( self.PZ, Magnitude)

		return UnitVector
		
