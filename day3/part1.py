import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

myinput = [(set(asd[:int(len(asd)/2)]), set(asd[int(len(asd)/2):])) for asd in myinput]
shared = [a[0].intersection(a[1]) for a in myinput]

vals = zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53))
vals = dict(vals)

priorities = [sum([vals[asd] for asd in a]) for a in shared]
print(sum(priorities))