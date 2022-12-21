import os
from collections import deque
from math import copysign

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
encrypted = [int(i) for i in myinput]

def decrypt(encrypted, mixes, key):
    encrypted = [val*key for val in encrypted]
    indices = deque(range(len(encrypted)))

    for m in range(mixes):
        for i in range(len(encrypted)):
            j = indices.index(i)
            val = encrypted[i]

            indices.remove(i)
            indices.rotate(-val)
            indices.insert(j, i)

    decrypted = deque([encrypted[i] for i in indices])
    return decrypted

def coordinates(decrypted):
    i = decrypted.index(0)
    decrypted.rotate(-i)
    coord = [decrypted[j % len(decrypted)] for j in [1000, 2000, 3000]]
    return coord

decrypted = decrypt(encrypted, 10, 811589153)
coordinates = coordinates(decrypted)
print(sum(coordinates))