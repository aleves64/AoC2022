import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

overlaps = 0
for line in myinput:
    first, second = line.split(",")
    first = [int(val) for val in first.split("-")]
    first = set(range(first[0],first[1]+1))
    second = [int(val) for val in second.split("-")]
    second = set(range(second[0],second[1]+1))
    if len(first.intersection(second)) != 0:
        overlaps += 1
print(overlaps)