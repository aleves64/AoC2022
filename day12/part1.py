import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
grid = myinput.split("\n")[:-1]

start, = [(i,line.index('S')) for i, line in enumerate(grid) if 'S' in line]
end, = [(i,line.index('E')) for i, line in enumerate(grid) if 'E' in line]

def get_ord(c):
    if c == 'S':
        val = ord('z')
    elif c == 'E':
        val = ord('z')+1
    else:
        val = ord(c)
    return val

def get_neighbors(node):
    global grid
    i, j = node
    val = get_ord(grid[i][j])
    neighbors = []
    if i > 0 and get_ord(grid[i - 1][j]) - val <= 1:
        neighbors.append((i - 1, j))
    if i < len(grid) - 1 and get_ord(grid[i + 1][j]) - val <= 1:
        neighbors.append((i + 1, j))
    if j > 0 and get_ord(grid[i][j - 1]) - val <= 1:
        neighbors.append((i, j - 1))
    if j < len(grid[i]) - 1 and get_ord(grid[i][j + 1]) - val <= 1:
        neighbors.append((i, j + 1))
    return neighbors

prev = {}
visited = set()
queue = deque([start])
while queue:
    node = queue.popleft()
    visited.add(node)
    if node == end:
        break

    neighbors = get_neighbors(node)
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        if not neighbor in prev:
            prev[neighbor] = node
            queue.append(neighbor)

node = end
steps = 0
while node in prev:
    i, j = node
    node = prev[node]
    steps += 1
print(steps)