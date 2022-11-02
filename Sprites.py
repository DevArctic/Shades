from pyglet.gl import *
import OpenGL
import math
import Tracks
import Movement

class Circle():
	def __init__(self):
		self.vertices = 0
		self.parent = []
		
	def setParent(self, parent):
		self.parent = parent

	def draw(self, ctx, MODE,filled=True):
		x, y = self.parent.getPos()			
		radius = self.parent.getSize()		
		r, g, b = self.parent.getColor()
		if MODE == 0:
			ctx.set_source_rgb(r, g, b)
			ctx.arc(x, y, radius, 0, 2*math.pi)
			if filled == True:
				ctx.fill()
			ctx.stroke()
			
class Expander():
	def __init__(self):
		self.parent = []
		self.color = (0,0,0)
		self.size = 1
		
	def setParent(self, parent):
		self.parent = parent
		
	def setColor(self):
		self.color = self.parent.color
	
	def increment(self, inc):
		self.size = self.size + inc
		
	def draw(self, ctx, MODE,filled=True):
		x, y = self.parent.getPos()			
		maxRadius = self.parent.getSize()
		r,g,b = self.color		
		if MODE == 0:
			ctx.set_source_rgb(r, g, b)
			ctx.arc(x, y, self.size, 0, 2*math.pi)
			if filled == True:
				ctx.fill()
			ctx.stroke()

class Square():
	def __init__(self):
		self.vertices = 0

	def draw(self, center, radius, ctx, MODE):
		x, y = center
		corner1 = (x-radius,y-radius)
		corner2 = (x+radius,y-radius)
		corner3 = (x+radius,y+radius)
		corner4 = (x-radius,y+radius)
		if MODE == 0:
			ctx.set_source_rgb(1,1,1)
			ctx.move_to(corner1[0],corner1[1])
			ctx.line_to(corner2[0],corner2[1])
			ctx.line_to(corner3[0],corner3[1])
			ctx.line_to(corner4[0],corner4[1])
			ctx.line_to(corner1[0],corner1[1])
			ctx.stroke()
			
class nGon():
	def __init__(self, center, radius, nverts):
		self.nverts = nverts
		self.radius = radius
		self.verts = Tracks.newCircle(center, radius, self.nverts)
		
	def draw(self, ctx, MODE):
		if MODE == 0:
			ctx.set_source_rgb(1,1,1)
			ctx.move_to(self.verts[0][0],self.verts[0][1])
			for x in range(len(self.verts)-1):
				cur = x + 1
				ctx.line_to(self.verts[cur][0],self.verts[cur][1])
			ctx.line_to(self.verts[0][0],self.verts[0][1])
			ctx.stroke()
	
	def turn(self, center, speed):
		for x in range(len(self.verts)):
			self.verts[x] = Movement.rotateAboutPoint(center, Movement.rad(speed), self.verts[x])
		

		
		
		
		
		
		
		
		 
