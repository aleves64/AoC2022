import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
cubes = set([tuple(int(val) for val in line.split(",")) for line in myinput])

total = 0
for cube in cubes:
    x,y,z = cube
    sides = 6
    sides -= (x+1,y,z) in cubes
    sides -= (x-1,y,z) in cubes
    sides -= (x,y+1,z) in cubes
    sides -= (x,y-1,z) in cubes
    sides -= (x,y,z+1) in cubes
    sides -= (x,y,z-1) in cubes
    total += sides
print(total)