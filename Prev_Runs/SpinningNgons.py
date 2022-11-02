import PyCairo
import Shades
import math
import Tracks
import Sprites
from pyglet.gl import *
import CairoPIL

NFRAMES = 240
#MODE 0 PYCAIRO

MODE = 0
SIZEX = 800
SIZEY = 800

RED = (0.941, 0, 0.172)
BLUE = (0.019, 0.180, 0.839)
GREEN = (0.019, 0.839, 0.149)
WHITE = (1,1,1)

tick = 0

pp = Shades.PolygonParent(7,240)
pp.clearShades()

pp.addShades([Shades.PolygonParent(x+3,240) for x in range(7)])
print (pp.shades)

for each in pp.shades:
	each.setSize((50))
pp.setPos((400,400))
pp.setSize((250))



def runSim(ctx):
	global tick
	pp.setShades()
	for each in pp.shades:
		each.setShades(-1)
	pp.drawShades(ctx,MODE)
	pp.incPhase(1)
	for each in pp.shades:
		each.incPhase(2)
	
	tick = tick + 1

frames =[]

if MODE == 0:
	surface = PyCairo.initSurface(SIZEX,SIZEY)
	ctx = PyCairo.initContext(surface)
	for x in range(NFRAMES):
		print("Rendering frame " + str(x) + "___")
		PyCairo.blankScreen(ctx,0,0,SIZEX,SIZEY)
		runSim(ctx)
		#PyCairo.render(surface,x)
		frames.append(CairoPIL.to_pil(surface))

frames[0].save("result.gif", save_all=True,append_images=frames[1:],duration=30,loop=0)
