import os
from itertools import combinations
from collections import deque
from functools import cache

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
cubes = set([tuple(int(val) for val in line.split(",")) for line in myinput])

def flood(source):
    visited = set()
    queue = deque([source])
    touched = set()
    while queue:
        v = queue.popleft()
        visited.add(v)
        x, y, z = v
        free, blocked = get_neighbors(v)
        touched = touched.union(blocked)
        for u in free:
            if u in visited or u in queue or outside_bounds(u):
                continue
            queue.append(u)
    return visited, touched

def outside_bounds(pos):
    x,y,z = pos
    return z > maxz or z < minz or y > maxy or y < miny or x > maxx or x < minx

@cache
def get_neighbors(pos):
    x, y, z = pos
    left = (x+1,y,z)
    right = (x-1,y,z)
    up = (x,y+1,z)
    down = (x,y-1,z)
    forward = (x,y,z+1)
    backward = (x,y,z-1)
    blocked = []
    free = []
    if left in cubes:
        blocked.append(left)
    else:
        free.append(left)
    if right in cubes:
        blocked.append(right)
    else:
        free.append(right)
    if up in cubes:
        blocked.append(up)
    else:
        free.append(up)
    if down in cubes:
        blocked.append(down)
    else:
        free.append(down)
    if forward in cubes:
        blocked.append(forward)
    else:
        free.append(forward)
    if backward in cubes:
        blocked.append(backward)
    else:
        free.append(backward)
    return free, blocked

minx, maxx = min([cube[0] for cube in cubes]), max([cube[0] for cube in cubes])
minx, maxx = minx - 1, maxx + 1
miny, maxy = min([cube[1] for cube in cubes]), max([cube[1] for cube in cubes])
miny, maxy = miny - 1, maxy + 1
minz, maxz = min([cube[2] for cube in cubes]), max([cube[2] for cube in cubes])
minz, maxz = minz - 1, maxz + 1

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        for z in range(minz, maxz+1):
            pos = (x,y,z)
            if not pos in cubes:
                break
visited, touched = flood(pos)
total = 0
for cube in touched:
    x,y,z = cube
    sides = 6
    sides -= (x+1,y,z) in cubes or not (x+1,y,z) in visited
    sides -= (x-1,y,z) in cubes or not (x-1,y,z) in visited
    sides -= (x,y+1,z) in cubes or not (x,y+1,z) in visited
    sides -= (x,y-1,z) in cubes or not (x,y-1,z) in visited
    sides -= (x,y,z+1) in cubes or not (x,y,z+1) in visited
    sides -= (x,y,z-1) in cubes or not (x,y,z-1) in visited
    total += sides
print(total)