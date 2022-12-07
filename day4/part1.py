import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

overlaps = 0
for line in myinput:
    first, second = line.split(",")
    first = [int(val) for val in first.split("-")]
    second = [int(val) for val in second.split("-")]
    if first[0] <= second[0] and first[1] >= second[1]:
        overlaps += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        overlaps += 1
print(overlaps)