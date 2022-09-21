import time
import math
from pyglet.gl import *



def rectangle(x, y, sx, sy):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x,y)
        glVertex2f(x,sy)
        glVertex2f(sx,sy)
        glVertex2f(sx,y)
        glEnd()

def makeCircle(numPoints, xCen, yCen, radius):
        verts = []
        for i in range(numPoints):
                angle = math.radians(float(i)/numPoints * 360.0)
                x = radius*math.cos(angle) + xCen
                y = radius*math.sin(angle) + yCen
                verts += [x,y]        
        return pyglet.graphics.vertex_list(numPoints, ('v2f', verts))

def makeSquare(x, y, radius):
        verts = []
        corner1 = [x-radius,y-radius]
        corner2 = [x+radius,y-radius]
        corner3 = [x+radius,y+radius]
        corner4 = [x-radius,y+radius]
        verts.extend(corner1)
        verts.extend(corner2)
        verts.extend(corner3)
        verts.extend(corner4)
        return pyglet.graphics.vertex_list(4, ('v2f',verts))
#@window.event
#def on_draw():
#        while True:
#                for x in range(100):
 #                       glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
  #                      glColor3f(1,0,0)
  #                      rectangle(0+x,0+x,45+x,45+x)
  #                      window.flip()

#pyglet.app.run()

makeCircle(10,5,5,5)