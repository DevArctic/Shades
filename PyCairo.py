import cairo
import os.path
import math
 
# setup a place to draw

def initSurface(x,y):
	surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, x, y)
	return surface

def initContext(surface):
	ctx = cairo.Context (surface)
	return ctx

def blankScreen(ctx,x,y,xx,yy):
	ctx.set_source_rgb(0, 0, 0)
	ctx.rectangle(x,y,xx,yy)
	ctx.fill()

def render(surface,x):
	current_directory = os.getcwd()
	final_directory = os.path.join(current_directory, r'Images')
	if not os.path.exists(final_directory):
		os.makedirs(final_directory)
	os.chdir(final_directory)
	surface.write_to_png('Frame' + str(x) + '.png') # write to file
	os.chdir(current_directory)