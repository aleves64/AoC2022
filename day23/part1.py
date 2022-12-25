import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
elves = set([(x,y) for y, line in enumerate(myinput) for x, c in enumerate(line) if c == '#'])

directions = deque([
  #axis #direction
    (1,-1), # North
    (1,1), # South
    (0,-1), # West
    (0,1)  # East
])

def swap(pos):
    x, y = pos
    return y, x

def is_available(elf, direction, elves):
    ax, dct = direction
    scan_along_ax = ax^1
    scan_on_ax = elf[ax] + dct
    for x in range(elf[scan_along_ax]-1,elf[scan_along_ax]+2):
        pos = (x, scan_on_ax)
        if ax == 0:
            pos = swap(pos)
        if pos in elves:
            return False
    return True

def count_empty(elves):
    xes = [elf[0] for elf in elves]
    startx, endx = min(xes), max(xes)
    yes = [elf[1] for elf in elves]
    starty, endy = min(yes), max(yes)
    empty_tiles = 0
    for x in range(startx, endx+1):
        for y in range(starty, endy+1):
            if not (x,y) in elves:
                empty_tiles += 1
    return empty_tiles

rounds = 0
while True:
    proposals = {}

    for elf in elves:
        available_positions = []
        for direction in directions:
            ax, dct = direction
            if is_available(elf, direction, elves):
                pos = (elf[ax^1], elf[ax]+dct)
                if ax == 0:
                    pos = swap(pos)
                available_positions.append(pos)
        if len(available_positions) == 4:
            continue
        elif len(available_positions) > 0:
            proposal = available_positions[0]
            if not proposal in proposals:
                proposals[proposal] = []
            proposals[proposal].append(elf)

    moves = 0
    for pos in proposals:
        if len(proposals[pos]) == 1:
            elf = proposals[pos][0]
            elves.remove(elf)
            elves.add(pos)
            moves += 1
    rounds += 1
    directions.rotate(-1)
    if rounds == 10:
        break
print(count_empty(elves))