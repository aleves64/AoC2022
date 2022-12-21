import os

with open("input", "r") as infile:
    myinput = infile.read()
jets = myinput[:-1]
jet_index = 0

shape0 = ["####"]
shape1 = [".#.","###",".#."]
shape2 = ["..#","..#","###"]
shape3 = ["#","#","#","#"]
shape4 = ["##","##"]
shapes = [shape0,shape1,shape2,shape3,shape4]

chamber = [list("#"*7), list("."*7)]

def move_horizontal(shape, pos, right=True):
    shape_height = len(shape)
    shape_width = len(shape[0])
    chamber_width = 7
    direction = 1 if right else -1

    x0, y0 = pos
    move_ok = True
    for dy in range(shape_height):
        for dx in range(shape_width):
            if shape[dy][dx] == '.':
                continue
            x1 = x0+dx + direction
            y1 = y0-dy
            if x1 < 0 or x1 >= chamber_width or chamber[y1][x1] == '#':
                move_ok = False
                break
        if not move_ok:
            break
    if move_ok:
        pos = x0+direction, y0
    return pos

def move_vertical(shape, pos):
    shape_height = len(shape)
    shape_width = len(shape[0])
    chamber_width = 7

    x0, y0 = pos
    move_ok = True
    for dy in range(shape_height):
        for dx in range(shape_width):
            if shape[dy][dx] == '.':
                continue
            x1 = x0+dx
            y1 = y0-dy - 1
            if y1 <= 0 or chamber[y1][x1] == '#':
                move_ok = False
                break
        if not move_ok:
            break
    if move_ok:
        pos = x0, y0 - 1
    return pos


def drop_shape(shape, max_y):
    global jet_index
    chamber_height = len(chamber) - 1
    required_height = max_y + 3 + len(shape)
    height_difference = required_height - chamber_height
    for i in range(0,height_difference):
        chamber.append(list("."*7))

    x = 2
    y = required_height

    prev_y = 0
    while y != prev_y:
        prev_y = y
        right = jets[jet_index%len(jets)] == ">"
        jet_index += 1
        x, y = move_horizontal(shape, (x,y), right)
        x, y = move_vertical(shape, (x,y))
    return x, y

def stop_shape(shape, pos):
    shape_height = len(shape)
    shape_width = len(shape[0])
    chamber_width = 7

    x0, y0 = pos
    for dy in range(shape_height):
        for dx in range(shape_width):
            if shape[dy][dx] == '.':
                continue
            x1 = x0+dx
            y1 = y0-dy
            chamber[y1][x1] = "#"

max_y = 0
for i in range(0, 2022):
    shape = shapes[i%5]
    x,y = drop_shape(shape, max_y)
    stop_shape(shape, (x,y))
    if y > max_y:
        max_y = y
print(max_y)