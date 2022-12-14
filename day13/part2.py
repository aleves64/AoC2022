import os
import functools

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

myinput.append([[2]])
myinput.append([[6]])
correct_order = sorted(myinput, key=functools.cmp_to_key(compare))
indices = []
for i, hurp in enumerate(correct_order):
    if hurp == [[2]] or hurp == [[6]]:
        indices.append(i+1)
print(indices[0]*indices[1])
