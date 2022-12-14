import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
paths = [[[int(coord) for coord in path.split(",")] for path in line.split(" -> ")] for line in myinput]

blocks = set()
source = (500,0)
abyss = 0

def order_swap(a,b):
    if a <= b:
        return (a,b)
    else:
        return (b,a)

for path in paths:
    for i in range(1, len(path)):
        end_x, end_y = path[i]
        start_x, start_y = path[i-1]
        start_x, end_x = order_swap(start_x, end_x)
        start_y, end_y = order_swap(start_y, end_y)
        dx = range(start_x, end_x+1)
        dy = range(start_y, end_y+1)
        for x in dx:
            blocks.add((x,start_y))
        for y in dy:
            blocks.add((start_x,y))
        if end_y > abyss:
            abyss = end_y
floor = abyss + 2

total = 0
y  = -1

while y != 0:
    x, y = source
    blocked = False
    while y+1 < floor:
        if not (x,y+1) in blocks:
            y = y + 1
        elif not (x-1,y+1) in blocks:
            x = x - 1
            y = y + 1
        elif not (x+1,y+1) in blocks:
            x = x + 1
            y = y + 1
        else:
            break
    blocks.add((x,y))
    total += 1
print(total)