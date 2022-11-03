import PyCairo
import Shades
import math
import Tracks
import Sprites
from pyglet.gl import *
import CairoPIL
import HexGrid

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



def runSim(ctx):
	global tick

	
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
