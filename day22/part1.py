import os
import re
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
grid, instructions = myinput.split("\n\n")
grid = grid.split("\n")
grid = [((row, column), char == '.') for row, line in enumerate(grid) for column, char in enumerate(line) if char in ['.','#']]
instructions = re.split(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)', instructions[:-1])
instructions = [(int(inst) if inst.isnumeric() else 0, 1 if inst == 'L' else -1 if inst == 'R' else 0) for inst in instructions]

def make_graph_by_order(sorted_grid, ax_i):
    graph = {}
    graph[sorted_grid[0]] = []
    start = 0
    for i in range(1, len(sorted_grid) + 1):
        prev = sorted_grid[i-1]
        if i == len(sorted_grid):
            current = (-1,-1), False
        else:
            current = sorted_grid[i]
        graph[current] = []
        if prev[0][ax_i] != current[0][ax_i]:
            wrapped = sorted_grid[start]
            graph[wrapped].insert(0,prev)
            graph[prev].append(wrapped)
            start = i
        else:
            graph[current].append(prev)
            graph[prev].append(current)
    return graph

def make_graph(grid):
    sorted_by_row = sorted(grid)
    sorted_by_column = sorted(grid, key = lambda x : x[0][1])
    graph0 = make_graph_by_order(sorted_by_row, 0) 
    graph1 = make_graph_by_order(sorted_by_column, 1)
    graph = {}
    for v in graph0:
        graph[v] = (graph0[v], graph1[v])
    return graph

graph = make_graph(grid)
orientations = deque([
    (0,1), # right
    (1,1), # down
    (0,0), # left
    (1,0)  # up
])
pos = grid[0]

for inst in instructions:
    axis, direction = orientations[0]
    steps, turn = inst
    orientations.rotate(turn)
    for i in range(steps):
        if graph[pos][axis][direction][1]:
            pos = graph[pos][axis][direction]

facing = orientations[0]
orientations.rotate(-orientations.index((0,1)))
facing = orientations.index(facing)
row, column = pos[0][0]+1, pos[0][1]+1

print(1000*row + 4*column + facing)