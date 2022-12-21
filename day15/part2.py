import os
from itertools import combinations
from math import sqrt

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
myinput = [line.split(" ") for line in myinput]

def parse(line, coord):
    res = line[coord].split("=")[1]
    if coord != -1:
        res = res[:-1]
    return int(res)
sensors = [[parse(line, coord) for coord in [2,3,-2,-1]] for line in myinput]

def rotate(x, y, reverse=False):
    switch = 1 if reverse else -1
    A00 = 1/sqrt(2)
    A01 = switch*-1/sqrt(2)
    A10 = switch*1/sqrt(2)
    A11 = 1/sqrt(2)
    new_x = A00*x + A01*y
    new_y = A10*x + A11*y
    return new_x, new_y

def get_corners(sensor):
    sx, sy, bx, by = sensor
    dx = abs(sx-bx)
    dy = abs(sy-by)
    dist = dx + dy
    sx1 = sx
    sx2 = sx
    sy1 = sy-dist
    sy2 = sy+dist+1
    return (sx1, sy1), (sx2, sy2)

def sensor_to_rect(sensor):
    corner1, corner2 = get_corners(sensor)
    x1, y1 = translate_point(corner1)
    x2, y2 = translate_point(corner2)
    rect = ((x1, y1), (x2, y2))
    return rect

def translate_point(point):
    x, y = point
    x, y = rotate(x, y)
    x = x * sqrt(2)
    y = y * sqrt(2)
    x = round(x)
    y = round(y)
    return x,y

def untranslate_point(point):
    x, y = point
    x = x / sqrt(2)
    y = y / sqrt(2)
    x, y = rotate(x, y, reverse=True)
    x = round(x)
    y = round(y)
    return x,y

rects = set()
for i in range(len(sensors)):
    sensor = sensors[i]
    rect = sensor_to_rect(sensor)
    rects.add(rect)

x_diffs = set()
for rect, other_rect in combinations(rects,2):
    (ax1, ay1), (ax2, ay2) = rect
    (bx1, by1), (bx2, by2) = other_rect
    if ax2+1 == bx1 or bx2+1 == ax1:
        x = min(ax2,bx2)
        break

y_diffs = set()
shared_1_diff = set()
for rect, other_rect in combinations(rects,2):
    (ax1, ay1), (ax2, ay2) = rect
    (bx1, by1), (bx2, by2) = other_rect
    if ay2+1 == by1 or by2+1 == ay1:
        y = min(ay2,by2)
        nx1 = min(ax1, bx1)
        nx2 = max(ax2, bx2)
        y_diffs.add(y)
        if x <= nx1 and x >= nx1:
            break

x,y = untranslate_point((x,y))
print(x*4000000 + y)