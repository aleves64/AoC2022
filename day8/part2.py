import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
grid = [ [int(i) for i in list(row)] for row in myinput]

total = 0
scores = []
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
        trees_from_top = 0
        trees_from_bottom = 0
        trees_from_left = 0
        trees_from_right = 0
        for k in range(i-1,-1,-1):
            trees_from_top += 1
            if grid[k][j] >= height:
                visible_from_top = False
                break
        for k in range(i+1, len(grid)):
            trees_from_bottom += 1
            if grid[k][j] >= height:
                visible_from_bottom = False
                break
        for l in range(j-1, -1, -1):
            trees_from_left += 1
            if grid[i][l] >= height:
                visible_from_left = False
                break
        for l in range(j+1, len(grid[i])):
            trees_from_right += 1
            if grid[i][l] >= height:
                visible_from_right = False
                break
        visible = visible_from_top or visible_from_bottom or visible_from_left or visible_from_right
        score = trees_from_top*trees_from_bottom*trees_from_left*trees_from_right
        scores.append(score)
        if visible:
            total += 1
print(total)
print(sorted(scores))