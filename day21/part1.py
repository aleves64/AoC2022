import os
import operator

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
lines = [line.split(" ") for line in myinput]

VALUE = 0
OPERATION = 1
expressions = {}
for line in lines:
    identifier = line[0][:-1]
    val = None
    leftop = None
    rightop = None
    op = None
    if len(line) == 2:
        exptype = VALUE
        val = int(line[1])
    else:
        exptype = OPERATION
        leftop = line[1]
        rightop = line[3]
        op = line[2]
    expressions[identifier] = (exptype, val, op, leftop, rightop)

operators = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv
}

def evaluate(identifier):
    exptype, val, op, leftop, rightop = expressions[identifier]
    if exptype == VALUE:
        return val
    else:
        left = evaluate(leftop)
        right = evaluate(rightop)
        operator = operators[op]
        val = operator(left, right)
        expressions[identifier] = (VALUE, val, None, None, None)
        return val

print(evaluate("root"))