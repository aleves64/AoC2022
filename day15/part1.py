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

beaconless = set()
targetrow = 10

for sensor in sensors:
    sx, sy, bx, by = sensor
    dx = abs(sx-bx)
    dy = abs(sy-by)
    dist = dx+dy
    for x in range(0,dist+1):
        start = sy - (dist-x)
        end = sy + (dist-x)
        if targetrow >= start and targetrow <= end:
            beaconless.add(sx+x)
            beaconless.add(sx-x)
    if by == targetrow:
        beaconless.remove(bx)
    if sy == targetrow:
        beaconless.remove(sx)
print(len(beaconless))