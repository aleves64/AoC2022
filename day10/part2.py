import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
commands = [line.split(" ") for line in myinput]

X = 1
prev_X = 1
signal_total = 0
cycle = 0
screen = ["."*40]*6
screen = [list(line) for line in screen]

for command in commands:
    addedcycles = 0
    prev_X = X
    if command[0] == "noop":
        addedcycles = 1
    elif command[0] == "addx":
        arg = int(command[1])
        X += arg
        addedcycles = 2

    for i in range(addedcycles):
        cycle += 1
        coord_x = (cycle-1)%40
        coord_y = int((cycle-1)/40)
        if coord_x in range(prev_X-1,prev_X+2):
            screen[coord_y][coord_x] = "#"

for line in screen:
    line = ''.join(line)
    print(line)