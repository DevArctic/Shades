import Shades

class Grid:
	def __init__(self, origin, radius=3, hexsize=40):
		self.radius = radius
		self.hexsize = hexsize
		self.diam = (radius - 1) * 2
		self.grid = [[[Shades.HexTile(self, (i,j,k),  for k in range(self.diam)] for j in range(self.diam)] for i in range(self.diam)]
		self.origin = origin
		self.originHex = (self.radius,self.radius,self.radius)
		self.simpleList = []
		
	def setSimpleList(self):
		for i in range(self.diam):
			for j in range(self.diam):
				for k in range(self.diam):
					self.simpleList.append(self.grid[i][j][k])
					
	def convert(self, cord):
		userx, usery, userz = cord
		gridx = userx + self.originHex[0]
		gridy = usery + self.originHex[1]
		gridz = userz + self.originHex[2]
		return (gridx,gridy,gridz)
		
	def getHex(self, cord):
		newCord = self.convert(cord)
		return self.grid[newCord[0]][newCord[1]][newCord[2]]
		

		
		
					
	
					

		
		
		
		
		
		

		
		
		
	
	
