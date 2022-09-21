import OpenGL
import math
import Sprites
import Tracks
from pyglet.gl import *

class Shade():
    def __init__(self,center,size,color,filled,MODE):
        self.center = center
        self.size = size
        self.MODE = MODE
        self.track = []
        self.sprites = []
        self.tick = 0
        self.trackTick = 0
        self.color = color
        self.filled = filled


    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def drawSprites(self, ctx):
        for each in self.sprites:
            each.draw(self.center, self.size, self.color, self.filled, ctx, self.MODE)

    def addTrack(self, track):
        self.track.extend(track)

    def moveOnTrack(self):
        try:
            self.center = self.track[self.trackTick]
        except:
            self.trackTick = 0
            self.center = self.track[self.trackTick]
        self.trackTick = self.trackTick + 1

    def addVar(self, variable, value):
        setattr(self, variable, value)

    def changeColor(self, newColor):
        self.color = newColor

        
class Follower(Shade):
    
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
