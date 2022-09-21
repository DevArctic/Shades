import math
import random

def oneDimLine(start, end, frames):
    start = start
    end = end
    i = (end - start)/frames
    track = []
    for x in range(frames):
        step = start + (i * x)
        track.append(step)
    return track

def newPoint(cords, frames):
    track = []
    for x in range(frames):
        track.append(cords)
    return track

def newLine(start, end, frames):
    startx, starty, = start
    endx, endy = end
    dx = endx - startx
    dy = endy - starty
    ix = dx/frames
    iy = dy/frames
    track = []
    for x in range(frames):
        stepx = startx + (ix * x)
        stepy = starty + (iy * x)
        track.append((stepx,stepy))
    return track

def newCircle(center, radius, frames):
    centerx, centery = center
    radian = (2 * math.pi)/frames
    track = []
    for slices in range(frames):
        x = (math.cos(radian * slices) * radius) + centerx
        y = (math.sin(radian * slices) * radius) + centery
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
    

    




