import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
key = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
reverse_key = {
    2 : '2',
    1 : '1',
    0 : '0',
    -1 : '-',
    -2 : '='
}

def renumerate(sequence, start=None):
    if start is None:
        start = len(sequence) - 1
    n = start
    for elem in sequence:
        yield n, elem
        n -= 1

def convert(number):
    val = 0
    for pos, digit in renumerate(number):
        val += key[digit]*5**pos
    return val

def deconvert(number):
    val = []
    maxdigit = list(key.values())[0]
    while number > 0:
        r = number % 5
        number = number // 5
        val.append(r)
    val.append(0)
    for i, d in enumerate(val):
        if d > maxdigit:
            val[i] = d-5
            val[i+1] += 1
    if val[-1] == 0:
        val.pop()
    return "".join([reverse_key[d] for d in val[::-1]])

values = []
for number in myinput:
    val = convert(number)
    values.append(val)
total = sum(values)
answer = deconvert(total)
print(answer)