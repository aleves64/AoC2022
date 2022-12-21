import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.replace("\n\n", ",").replace("\n", ",")[:-1]
myinput = eval("[" + myinput + "]")

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    for i in range(min(len(left), len(right))):
        comp = compare(left[i],right[i])
        if comp < 0:
            return -1
        elif comp > 0:
            return 1
    if len(left) < len(right):
        return -1
    elif len(right) < len(left):
        return 1
    else:
        return 0

correct = []
for i in range(0, len(myinput), 2):
    left = myinput[i]
    right = myinput[i+1]
    if compare(left, right) < 0:
        correct.append(int(i/2) + 1)
print(sum(correct))