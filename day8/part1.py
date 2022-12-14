import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
grid = [ [int(i) for i in list(row)] for row in myinput]

total = 0
for i in range(len(grid)):
    if i == 0 or i == len(grid)-1:
        total += len(grid[i])
        continue
    for j in range(len(grid[i])):
        if j == 0 or j == len(grid[i])-1:
            total += 1
            continue
        height = grid[i][j]
        visible_from_top = True
        visible_from_bottom = True
        visible_from_left = True
        visible_from_right = True
        for k in range(0,i):
            if grid[k][j] >= height:
                visible_from_top = False
                break
        for k in range(i+1,len(grid)):
            if grid[k][j] >= height:
                visible_from_bottom = False
                break
        for l in range(0,j):
            if grid[i][l] >= height:
                visible_from_left = False
                break
        for l in range(j+1,len(grid[i])):
            if grid[i][l] >= height:
                visible_from_right = False
                break
        visible = visible_from_top or visible_from_bottom or visible_from_left or visible_from_right
        if visible:
            total += 1
print(total)