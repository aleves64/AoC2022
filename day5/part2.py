import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
moves = myinput[1].split("\n")[:-1]
towers = myinput[0].split("\n")[:-1]

stacks = []
for line in towers:
    for i in range(1,len(line),4):
        if line[i] != ' ':
            index = int((i-1)/4)
            while len(stacks) < index+1:
                stacks.append(deque())
            stacks[index].append(line[i])

for command in moves:
    command = command.split(" ")
    count = int(command[1])
    src = int(command[3])
    src = stacks[src-1]
    dst = int(command[5])
    dst = stacks[dst-1]
    items = deque()
    for i in range(count):
        items.appendleft(src.popleft())
    for i in range(len(items)):
        dst.appendleft(items.popleft())

for stack in stacks:
    print(stack[0])