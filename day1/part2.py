import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")
myinput = [ sum([int(num) for num in nums.split("\n") if num ]) for nums in myinput]
print(sum(sorted(myinput)[-3:]))