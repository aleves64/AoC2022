import os
from math import sqrt
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
commands = deque()

for line in myinput:
    line = line.split(" ")
    move = line[0]
    amount = int(line[1])
    for i in range(amount):
        commands.append(move)

def head_move(command, pos):
    x, y = pos
    if command == 'L':
        x -= 1
    elif command == 'R':
        x += 1
    elif command == 'U':
        y -= 1
    elif command == 'D':
        y += 1
    return (x, y)

def tail_move(current, prev):
    current_x, current_y = current
    prev_x, prev_y = prev

    dx = prev_x - current_x
    dy = prev_y - current_y

    dist = sqrt(dx**2 + dy**2)
    if dist <= sqrt(2):
        return current

    if dx > 0:
        current_x += 1
    elif dx < 0:
        current_x -= 1
    if dy > 0:
        current_y += 1
    elif dy < 0:
        current_y -= 1
    return (current_x,current_y)

snake_n = 2
snake = [(0,0)]*snake_n
visited = set([(0,0)])

while commands:
    command = commands.popleft()
    snake[0] = head_move(command, snake[0])
    for i in range(1,snake_n):
        current = snake[i]
        prev = snake[i-1]
        snake[i] = tail_move(current, prev)
        if i == snake_n - 1:
            visited.add(snake[i])
print(len(visited))