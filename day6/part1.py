import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput[:-1]

queue = deque()
for i in range(3):
    c = myinput[i]
    queue.append(c)
for i in range(3,len(myinput)):
    c = myinput[i]
    queue.append(c)
    asd = sorted(queue)
    duplicates=False
    for j in range(1,len(asd)):
        if asd[j-1] == asd[j]:
            duplicates = True
    if duplicates:
        queue.popleft()
    else:
        break
print(i+1)