import PyCairo
import Shades
import math
import Tracks
import Sprites
from pyglet.gl import *

FRAMES = 240
MODE = 1
SIZEX = 800
SIZEY = 800

RED = (0.941, 0, 0.172)
BLUE = (0.019, 0.180, 0.839)
GREEN = (0.019, 0.839, 0.149)
WHITE = (1,1,1)

tick = 0

t1 = Tracks.newCircle((400,400), 200, FRAMES)

bf = Tracks.backAndForthSin(120)
print(bf)
bf.extend(bf)

tc1 = Tracks.twoColorTrack(RED, WHITE, FRAMES//2)
tc2 = Tracks.twoColorTrack(BLUE, WHITE, FRAMES//2)
tc3 = Tracks.twoColorTrack(GREEN, WHITE, FRAMES//2)

s1 = Shades.Shade(t1[0],25,RED, True, MODE)
s2 = Shades.Shade(t1[80],25,BLUE,True,MODE)
s3 = Shades.Shade(t1[160],25,GREEN,True,MODE)

p1 = Sprites.Circle()
p2 = Sprites.Circle()
p3 = Sprites.Circle()

s1.addSprite(p1)
s2.addSprite(p2)
s3.addSprite(p3)
s1.addTrack(t1)
s2.addTrack(t1)
s3.addTrack(t1)
s2.trackTick = 80
s3.trackTick = 160

s11 = Shades.Orbiter(t1[0],10,RED,True,MODE,80)
s22 = Shades.Orbiter(t1[0],10,BLUE, True,MODE,80)
s33 = Shades.Orbiter(t1[0],10,GREEN, True, MODE,80)
p11 = Sprites.Circle()
p22 = Sprites.Circle()
p33 = Sprites.Circle()
s11.addSprite(p11)
s22.addSprite(p22)
s33.addSprite(p33)
s11.tick = 46
s22.tick = 37
s33.tick = 112


def runSim(ctx):
    global tick
    s1.drawSprites(ctx)
    s2.drawSprites(ctx)
    s3.drawSprites(ctx)
    s1.moveOnTrack()
    s2.moveOnTrack()
    s3.moveOnTrack()
    s11.updateAndDraw(s1,FRAMES//2,ctx)
    s22.updateAndDraw(s2,FRAMES//3,ctx)
    s33.updateAndDraw(s3,FRAMES//2,ctx)
    s1.changeColor(tc1[bf[tick]])
    try:
        s2.changeColor(tc2[bf[tick+80]])
    except:
        s2.changeColor(tc2[bf[tick-160]])
    try:
        s3.changeColor(tc3[bf[tick+160]])
    except:
        s3.changeColor(tc3[bf[tick-80]])


    tick = tick + 1


if MODE == 0:
    surface = PyCairo.initSurface(SIZEX,SIZEY)
    ctx = PyCairo.initContext(surface)
    for x in range(FRAMES):
        PyCairo.blankScreen(ctx,0,0,SIZEX,SIZEY)
        runSim(ctx)
        PyCairo.render(surface,x)

elif MODE == 1:
    window = pyglet.window.Window(SIZEX, SIZEY)
    
    

    @window.event
    def on_draw():
        for x in range(FRAMES):
            window.flip()
            glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
            runSim(0)
            
       
       

    pyglet.app.run()

Tracks.colorChanger(10,FRAMES)