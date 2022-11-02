import math
import random

def point(cord, frames):
	""" No movement. No sound. Nothing. Complete
	stillness. """
	track = []
	for frame in range(frames):
		track.append(cord)
	return track
	
def one_dimensional_line(start, end, frames):
	""" Within the space between two points exist
	an uncountably infinite number of points. """
	start = start
	end = end
	d = end - start
	i = d/frames
	track = []
	for frame in range(frames):
		step = start + (i * frame)
		track.append(step)
	return track

def two_dimensional_line(start, end, frames):
	""" ...between two points within a two-dimensional space. """
	startx, starty, = start
	endx, endy = end
	dx = endx - startx
	dy = endy - starty
	ix = dx/frames
	iy = dy/frames
	track = []
	for frame in range(frames):
		stepx = startx + (ix * frame)
		stepy = starty + (iy * frame)
		track.append((stepx,stepy))
	return track
	
def three_dimensional_line(start, end, frames):
	""" ...between two points within a three-dimensional space. """
	startx, starty, startz = start
	endx, endy, endz = end
	dx = endx - startx
	dy = endy - starty
	dz = endz - startz
	ix = dx/frames
	iy = dy/frames
	iz = dz/frames
	track = []
	for frame in range(frames):
		stepx = startx + (ix * frame)
		stepy = starty + (iy * frame)
		stepz = startz + (iz * frame)
		track.append((stepx,stepy,stepz))
	return track

def Circle(center, radius, frames, phase=0, phasediv=1,wise=1):
	centerx, centery = center
	phrad = (2 * math.pi)/phasediv
	radian = (2 * math.pi)/frames
	track = []
	for slices in range(frames):
		x = (math.cos((radian * slices) +(phrad * phase)) * radius) + centerx
		y = (math.sin((radian * slices) +(phrad * phase)) * wise * radius) + centery
		track.append((x,y))
	return track

def twoColorTrack(startColor, endColor, frames):
	r1, g1, b1 = startColor
	r2, g2, b2 = endColor
	track = []
	rt = oneDimLine(r1,r2,frames)
	gt = oneDimLine(g1,g2,frames)
	bt = oneDimLine(b1,b2,frames)
	for x in range(frames):
		combined = (rt[x],gt[x],bt[x])
		track.append(combined)
	return track

def backAndForth(frames):
	track = []
	for x in range(frames//2):
		track.append(x)
	for x in range(frames//2):
		track.append((frames//2)-x)
	return track

def backAndForthSin(frames):
	track = []
	for x in range(frames):
		radian = (2*math.pi)/frames
		track.append(abs(round(math.sin(radian * x) * frames//2)))
	print(track)
	return track
	


def colorChanger(speed, frames):
	speed = speed
	track = []
	r = random.random()
	g = random.random()
	b = random.random()
	track.append((r,g,b))
	while len(track) < frames-speed:
		r2 = random.random()
		ir = (r2 - track[-1][0])/speed
		g2 = random.random()
		ig = (g2 - track[-1][1])/speed
		b2 = random.random()
		ib = (b2 - track[-1][2])/speed
		rstop = track[-1][0]
		gstop = track[-1][1]
		bstop = track[-1][2]
		for x in range(speed):
			stepr = rstop + (ir * x)
			stepg = gstop + (ig * x)
			stepb = bstop + (ib * x)
			track.append((stepr,stepg,stepb))
	track.pop(0)
	if len(track) == frames-speed:
		ir = (r - track[-1][0])/speed
		ig = (g - track[-1][1])/speed
		ib = (b - track[-1][2])/speed
		rstop = track[-1][0]
		gstop = track[-1][1]
		bstop = track[-1][2]
		for x in range(speed):
			stepr = rstop + (ir * x)
			stepg = gstop + (ig * x)
			stepb = bstop + (ib * x)
			track.append((stepr,stepg,stepb))

	return track
	
def mvPhase(track, offset):
	return track[offset::] + track[:offset:]

def rainbowWalk(footfalls):
	track = []
	foots = footfalls//6
	track.extend(three_dimensional_line((0.25,1,0.25),(0.25,1,1),foots))
	track.extend(three_dimensional_line((0.25,1,1),(0.25,0.25,1),foots))
	track.extend(three_dimensional_line((0.25,0.25,1),(1,0.25,1),foots))
	track.extend(three_dimensional_line((1,0.25,1),(1,0.25,0.25),foots))
	track.extend(three_dimensional_line((1,0.25,0.25),(1,1,0.25),foots))
	track.extend(three_dimensional_line((1,1,0.25),(0.25,1,0.25),foots))
	return track

def runParallel(track1,track2):
	parallels = []
	for x in len(track1):
		parallels.append((track1[x],track2[x]))
	return parallels
		

