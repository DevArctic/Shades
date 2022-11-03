import OpenGL
import math
import Sprites
import Tracks
from pyglet.gl import *

class Shade():
	""" A Shade is the underlying truth of things. For instance, you do not
	really know a person, you know a representation of a person which has been
	presented to you. The inner self, the so called ghost in the machine, is
	completely out of your ability to comprehend. It is the Form that gives rise
	to appearances. The Shade is real. Its appearance is not. """
	def __init__(self,size=1):
		self.pos = (0,0)
		self.size = 0
		self.track = []
		self.sprites = []
		self.tick = 0
		self.trackTick = 0
		self.color = (0,0,0)
		self.filled = False 
		self.shades = []

	def getPos(self):
		return self.pos
	
	def setPos(self, newpos):
		self.pos = newpos

	def setChildPos(self, track):
		for each in self.shades:
			each.setPos(track[x])
		
	def getSize(self):
		return self.size
		
	def setSize(self,newsize):
		self.size = newsize
		
	def getColor(self):
		return self.color
		
	def setColor(self,color):
		self.color = color

	def addShade(self, shade):
		self.shades.append(shade)

	def addShades(self, shades):
		self.shades.extend(shades)

	def clearShades(self):
		self.shades = []

	def draw(self, ctx, MODE):
		self.drawSprites(ctx, MODE)
		self.drawShades(ctx,MODE)

	def addSprite(self, sprite):
		""" One can always get at the nature of a Shade by providing it with
		an appearance, a cloak that makes the invisible visible. Do not confuse
		the two. """
		sprite.setParent(self)
		self.sprites.append(sprite)
		
	def addSprites(self, sprites):
		for each in sprites:
			each.setParent(self)
			self.sprites.append(each)
		

	def drawShades(self,ctx,MODE):
		for each in self.shades:
			each.draw(ctx,MODE)

	def drawSprites(self, ctx, MODE):
		for each in self.sprites:
			each.draw(ctx, MODE)

	def addTrack(self, track):
		self.track.extend(track)

	def setStart(self):
		self.pos = self.track[0]

	def moveOnTrack(self):
		try:
			self.pos = self.track[self.trackTick]
		except:
			self.trackTick = 0
			self.pos = self.track[self.trackTick]
		self.trackTick = self.trackTick + 1

	def addVar(self, variable, value):
		setattr(self, variable, value)

	def changeColor(self, newColor):
		self.color = newColor

class PolygonParent(Shade):
	def __init__(self, nverts, phasediv, size=1):
		super().__init__()
		self.shades = [Shade() for x in range(nverts)]
		self.phase = 0
		self.phasediv = phasediv
		self.nverts = nverts

	def setShades(self, wise=1):
		verts = Tracks.Circle(self.pos,self.size,self.nverts,phase=self.phase,phasediv=self.phasediv, wise=wise)
		for x in range(self.nverts):
			self.shades[x].setPos(verts[x])
	
	def incPhase(self, inc):
		self.phase = self.phase + inc

	def draw(self,ctx,MODE):
		m = MODE
		ctx.set_source_rgb(1,1,1)
		ctx.move_to(self.shades[0].getPos()[0],self.shades[0].getPos()[1])
		for x in range(len(self.shades)-1):
			cur = x + 1
			ctx.line_to(self.shades[cur].getPos()[0],self.shades[cur].getPos()[1])
		ctx.line_to(self.shades[0].getPos()[0],self.shades[0].getPos()[1])
		ctx.stroke()
		self.drawShades(ctx,MODE)
		self.drawSprites(ctx,MODE)

class HexTile(Shade):
	def __init__(self, parent):
		 self.parent=parent
	

		
class Follower(Shade):
	""" There is a certain comfort in never making your own
	decisions. Who can blame one for eschewing agency for
	knowing the path one treads is safe and warm? """
	
	def updateAndDraw(self, Leader, delay, ctx):
		if self.tick == delay:
			crumb = Leader.center
			self.track.append(crumb)
			self.moveOnTrack()
			self.drawSprites(ctx)
		elif self.tick < delay:
			crumb = Leader.center
			self.track.append(crumb)
			self.tick = self.tick + 1
			self.drawSprites(ctx)

class Orbiter(Shade):
	def __init__(self, center, size, color, filled, MODE, distanceOut):
		Shade.__init__(self,center,size, color, filled, MODE)
		self.dOut = distanceOut

	def updateAndDraw(self, Leader, frames, ctx):
		t1 = Tracks.newCircle(Leader.center,self.dOut,frames)
		try:
			self.center = t1[self.tick]
		except IndexError:
			self.tick = 0
			self.center = t1[self.tick]
		self.tick = self.tick + 1
		self.drawSprites(ctx)
