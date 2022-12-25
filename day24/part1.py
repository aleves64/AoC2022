import os
from collections import deque
from itertools import repeat

with open("input", "r") as infile:
    myinput = infile.read()
grid = myinput.split("\n")[:-1]
directions = {
  #axis #direction
    '^': (1,-1), # North
    'v': (1,1), # South
    '<': (0,-1), # West
    '>': (0,1)  # East
}
blizzards = set([((x,y), directions[c]) for y, line in enumerate(grid) for x, c in enumerate(line) if c in directions])
width = len(grid[0])
height = len(grid)

def swap(pos):
    x, y = pos
    return y, x

def get_next_blizzards(blizzards):
    next_blizzards = set()
    for blizzard in blizzards:
        pos = blizzard[0]
        ax, dct = blizzard[1]
        x, y = pos[ax^1], pos[ax] + dct
        if ax == 0:
            x, y = y, x
        if x < 1:
            x = width-2
        elif x > width-2:
            x = 1
        elif y < 1:
            y = height-2
        elif y > height-2:
            y = 1
        pos = x, y
        next_blizzard = (pos, blizzard[1])
        next_blizzards.add(next_blizzard)
    return next_blizzards

def get_neighbors(pos, blizzard_state):
    x, y = pos
    neighbors = []
    
    if x > 0 and grid[y][x-1] != '#' and not (x-1, y) in blizzard_state:
        neighbors.append((x-1, y))
    if x < width-1 and grid[y][x+1] != '#' and not (x+1, y) in blizzard_state:
        neighbors.append((x+1, y))
    if y > 0 and grid[y-1][x] != '#' and not (x, y-1) in blizzard_state:
        neighbors.append((x, y-1))
    if y < height-1 and grid[y+1][x] != '#' and not (x, y+1) in blizzard_state:
        neighbors.append((x, y+1))
    if not (x,y) in blizzard_state:
        neighbors.append((x, y))
    return neighbors

def get_blizzard_states():
    blizzard_states = [blizzards]
    state = blizzards
    while True:
        state = get_next_blizzards(state)
        if state == blizzard_states[0]:
            break
        blizzard_states.append(state)
    blizzard_states = [set([pos for pos, direction in state]) for state in blizzard_states]
    return blizzard_states

blizzard_states = get_blizzard_states()
start = (grid[0].index("."),0)
end = (grid[-1].index("."),height-1)
initial_state = (start, 0)

queue = deque([initial_state])
explored = set([initial_state])
dist = {initial_state : 0}

while queue:
    state = queue.popleft()
    pos, blizzard_i = state
    if pos == end:
        break
    blizzard_i_next = (blizzard_i + 1) % len(blizzard_states)
    blizzard_state = blizzard_states[blizzard_i_next]
    neighbors = zip(get_neighbors(pos, blizzard_state), repeat(blizzard_i_next))
    for neighbor in neighbors:
        if not neighbor in explored:
            explored.add(neighbor)
            dist[neighbor] = dist[state] + 1
            queue.append(neighbor)
print(dist[state])