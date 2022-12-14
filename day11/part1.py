import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
lines = [line.split("\n")[:6] for line in myinput.split("\n\n")]

def get_operation(operation):
    operators = {
        '+': lambda a, b : a + b,
        '*': lambda a, b : a * b
    }
    a, op, b = operation.split("= ")[-1].split(" ")
    return lambda old : operators[op](old, old if b == "old" else int(b))

def create_monkey(title, items, operation, test, true_dest, false_dest):
    items = deque(map(int, items.split(":")[-1].split(",")))
    operation = get_operation(operation)
    test = int(test.split(" ")[-1])
    true_dest = int(true_dest.split(" ")[-1])
    false_dest = int(false_dest.split(" ")[-1])
    monkey = {
        "items": items,
        "operation": operation,
        "test": test,
        "true_dest": true_dest,
        "false_dest": false_dest
    }
    return monkey

monkeys = [create_monkey(*line) for line in lines]
before_test = lambda x : int(x / 3)
handled = [0]*len(monkeys)

for i in range(20):
    for m, monkey in enumerate(monkeys):
        items = monkey["items"]
        handled[m] += len(items)
        while items:
            item = items.popleft()
            op = monkey["operation"]
            test = monkey["test"]

            item = op(item)
            item = before_test(item)
            test_result = item % test

            dest = monkey["true_dest"] if test_result == 0 else monkey["false_dest"]
            monkeys[dest]["items"].append(item)

handled = sorted(handled)
score = handled[-1] * handled[-2]
print(score)