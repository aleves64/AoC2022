import os
import operator

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
lines = [line.split(" ") for line in myinput]

CONST = 0
OPERATION = 1
VARIABLE = 2
expressions = {}
for line in lines:
    identifier = line[0][:-1]
    val = None
    leftop = None
    rightop = None
    op = None
    if identifier == "humn":
        exptype = VARIABLE
    elif len(line) == 2:
        exptype = CONST
        val = int(line[1])
    else:
        exptype = OPERATION
        leftop = line[1]
        rightop = line[3]
        if identifier == "root":
            op = '-'
        else:
            op = line[2]
    expressions[identifier] = (exptype, val, op, leftop, rightop)

operators = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv
}

differentiation_operators = {
    '*': lambda f, fprime, g, gprime : fprime*g + f*gprime,
    '+': lambda f, fprime, g, gprime : fprime + gprime,
    '-': lambda f, fprime, g, gprime : fprime - gprime,
    '/': lambda f, fprime, g, gprime : (fprime*g - f*gprime)/(g**2)
}

def evaluate(identifier):
    exptype, val, op, leftop, rightop = expressions[identifier]
    if exptype != OPERATION:
        return val
    else:
        left = evaluate(leftop)
        right = evaluate(rightop)
        oper = operators[op]
        val = oper(left, right)
        return val

def differentiate(identifier):
    exptype, val, op, leftop, rightop = expressions[identifier]
    if exptype == VARIABLE:
        return 1
    elif exptype == CONST:
        return 0
    else:
        f = evaluate(leftop)
        fprime = differentiate(leftop)
        g = evaluate(rightop)
        gprime = differentiate(rightop)
        oper = differentiation_operators[op]
        val = oper(f, fprime, g, gprime)
        return val

def evaluate_at(identifier, x):
    expressions["humn"] = (VARIABLE, x, None, None, None)
    val = evaluate(identifier)
    return val

def differentiate_at(identifier, x):
    expressions["humn"] = (VARIABLE, x, None, None, None)
    val = differentiate(identifier)
    return val

def newton_method():
    x = 100
    prev = 10
    while True:
        prev = x
        x = x - evaluate_at("root", x)/differentiate_at("root", x)
        diff = abs(prev - x)
        if diff < 0.1:
            return round(x)

print(newton_method())