from pyglet.gl import *
import OpenGL
import math

class Circle():
    def __init__(self):
        self.vertices = 0

    def draw(self, center, size, color, filled, ctx, MODE):
        x, y = center
        r, g, b = color
        if MODE == 0:
            ctx.set_source_rgb(r, g, b)
            ctx.arc(x, y, size, 0, 2*math.pi)
            if filled == True:
                ctx.fill()
            ctx.stroke()
            print ("Creating Frame")
        elif MODE == 1:
            glColor3f(r,g,b)
            self.vertices = OpenGL.makeCircle(200,x,y,size) 
            if filled == False:
                self.vertices.draw(GL_LINE_LOOP)
            elif filled == True:
                self.vertices.draw(GL_TRIANGLE_FAN)
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
        elif MODE == 1:
            glColor3f(1,1,1)
            self.vertices = OpenGL.makeSquare(x,y,radius)
            self.vertices.draw(GL_LINE_LOOP)