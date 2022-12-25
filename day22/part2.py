import os
import re
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
grid, instructions = myinput.split("\n\n")
grid = grid.split("\n")
gfx = [list(line) for line in grid]
instructions = re.split(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)', instructions[:-1])
instructions = [(int(inst) if inst.isnumeric() else 0, 1 if inst == 'L' else -1 if inst == 'R' else 0) for inst in instructions]

cube_side = 50
side = 0
sides_handled = 0
pos_to_side = {}
sides = [[] for i in range(6)]
for row, line in enumerate(grid):
    emptyspace = 0
    for column, c in enumerate(line):
        if c == ' ':
            emptyspace += 1
            continue
        side = sides_handled + (column - emptyspace) // cube_side
        point = ((row,column),c=='.')
        sides[side].append(point)
        pos_to_side[point] = side
    if (row+1) % cube_side == 0:
        sides_handled += (len(line) - emptyspace) // cube_side

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
        if prev[0][ax_i] == current[0][ax_i]:
            graph[current].append(prev)
            graph[prev].append(current)
    return graph

def make_side_graph(grid):
    sorted_by_row = sorted(grid)
    sorted_by_column = sorted(grid, key = lambda x : x[0][1])
    graph0 = make_graph_by_order(sorted_by_row, 0) 
    graph1 = make_graph_by_order(sorted_by_column, 1)
    graph = {}
    for v in graph0:
        graph[v] = (graph0[v], graph1[v])
    return graph

def get_edge_points(side, edge):
    if edge == 'right' or edge == 'left':
        ax = 0
    else:
        ax = 1
    if edge == 'top' or edge == 'left':
        relevant_points = sorted(side, key = lambda x : x[0][not ax])[:cube_side]
    else:
        relevant_points = sorted(side, key = lambda x : x[0][not ax])[-cube_side:]
    return relevant_points, ax

def add_side_connections(graph, left_side, edge1, right_side, edge2, upside_down=False):
    left_right, ax_1 = get_edge_points(left_side, edge1)
    right_left, ax_2 = get_edge_points(right_side, edge2)
    if upside_down:
        right_left = list(reversed(right_left))
    for i in range(cube_side):
        if edge1 == 'top' or edge1 == 'left':
            graph[left_right[i]][ax_1].insert(0, right_left[i])
        else:
            graph[left_right[i]][ax_1].append(right_left[i])
        if edge2 == 'top' or edge2 == 'left':
            graph[right_left[i]][ax_2].insert(0, left_right[i])
        else:
            graph[right_left[i]][ax_2].append(left_right[i])

def make_cube(sides):
    graph = {}
    for side in sides:
        side_graph = make_side_graph(side)
        graph.update(side_graph)
    add_side_connections(graph, sides[0], "right", sides[1], "left")
    add_side_connections(graph, sides[3], "right", sides[4], "left")
    add_side_connections(graph, sides[1], "right", sides[4], "right", upside_down=True)
    add_side_connections(graph, sides[3], "left", sides[0], "left", upside_down=True)

    add_side_connections(graph, sides[0], "bottom", sides[2], "top")
    add_side_connections(graph, sides[2], "bottom", sides[4], "top")
    add_side_connections(graph, sides[3], "bottom", sides[5], "top")
    add_side_connections(graph, sides[5], "bottom", sides[1], "top")

    add_side_connections(graph, sides[0], "top", sides[5], "left")
    add_side_connections(graph, sides[4], "bottom", sides[5], "right")
    add_side_connections(graph, sides[1], "bottom", sides[2], "right")
    add_side_connections(graph, sides[3], "top", sides[2], "left")
    return graph

graph = make_cube(sides)
orientations = deque([
    (0,1), # right
    (1,1), # down
    (0,0), # left
    (1,0)  # up
])
side_change_turns = {
    (0,5) : -1, # up -> right
    (5,0) : 1,  # left -> down
    (4,5) : -1, # down -> left
    (5,4) : 1,  # right -> up
    (3,2) : -1, # up -> right
    (2,3) : 1,  # left -> down
    (2,1) : 1,  # right -> up
    (1,2) : -1,  # down -> left

    (0,3) : 2,  # left -> right
    (3,0) : 2,  # left -> left
    (4,1) : -2, #  right -> left
    (1,4) : -2 #  right -> left
}
pos = sides[0][0]

for inst in instructions:
    axis, direction = orientations[0]
    steps, turn = inst
    orientations.rotate(turn)
    for i in range(steps):
        if graph[pos][axis][direction][1]:
            prev_side = pos_to_side[pos]
            pos = graph[pos][axis][direction]
            side = pos_to_side[pos]
            if (prev_side, side) in side_change_turns:
                orientations.rotate(side_change_turns[(prev_side,side)])
                axis, direction = orientations[0]

facing = orientations[0]
orientations.rotate(-orientations.index((0,1)))
facing = orientations.index(facing)
row, column = pos[0][0]+1, pos[0][1]+1

print(1000*row + 4*column + facing)