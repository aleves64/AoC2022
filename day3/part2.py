import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

vals = zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53))
vals = dict(vals)

groups = []
for i in range(0,len(myinput),3):
    a = set(myinput[i])
    b = set(myinput[i+1])
    c = set(myinput[i+2])
    shared = a.intersection(b.intersection(c))
    (shared,) = shared
    val = vals[shared]
    groups.append(val)
print(sum(groups))