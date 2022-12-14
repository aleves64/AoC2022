import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
commands = [line.split(" ") for line in myinput]

X = 1
signal_total = 0
cycle = 0
prevX = 0
threshold = 20
step = 40
end = 220

for command in commands:
    print(f"{cycle} {X}")
    prevX = X
    if command[0] == "noop":
        cycle += 1
    elif command[0] == "addx":
        arg = int(command[1])
        X += arg
        cycle += 2

    if cycle >= threshold:
        signal = threshold * prevX
        print(signal)
        signal_total += signal
        threshold += step
    if threshold > 220:
        break
print(signal_total)