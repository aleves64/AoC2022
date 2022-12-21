import os
from functools import cache
from functools import reduce
import operator

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:3]
lines = [line.split(" ") for line in myinput]
blueprints = [[(int(line[6]), 0, 0, 0), (int(line[12]), 0, 0, 0), (int(line[18]), int(line[21]), 0, 0), (int(line[27]), 0, int(line[30]), 0)] for line in lines]
max_costs = [[max([device[i] for device in blueprint]) for i in range(3)]for blueprint in blueprints]

def renumerate(sequence, start=None):
    if start is None:
        start = len(sequence) - 1
    n = start
    for elem in sequence[::-1]:
        yield n, elem
        n -= 1

@cache
def search(blueprint_i, remaining_time, resources, bots):
    global best_observed
    global blueprints
    global max_costs

    geodes = resources[3]
    geodebots = bots[3]

    if remaining_time == 0:
        if geodes > best_observed[blueprint_i]:
            best_observed[blueprint_i] = geodes
        return geodes

    upper_bound = geodes + geodebots*remaining_time + (remaining_time-1)*remaining_time//2
    if upper_bound < best_observed[blueprint_i]:
        return 0

    best_score = 0
    for i, costs in renumerate(blueprints[blueprint_i]):
        if any(resources[j] - costs[j] < 0 for j in range(4)):
            continue
        if i < 3 and max_costs[blueprint_i][i] <= bots[i]:
            continue

        next_resources = tuple(resources[j] + bots[j] - costs[j] for j in range(4))
        next_bots = bots[:i] + (bots[i]+1,) + bots[i+1:]

        candidate_score = search(blueprint_i, remaining_time - 1, next_resources, next_bots)
        best_score = max(best_score, candidate_score)
        if i == 3:
            return best_score

    candidate_score = search(blueprint_i, remaining_time - 1, tuple(resources[i] + bots[i] for i in range(4)), bots)
    best_score = max(best_score, candidate_score)

    return best_score

blueprint_scores = []
best_observed = {}
for i in range(len(blueprints)):
    best_observed[i] = 0
    resources = (0,0,0,0)
    bots = (1,0,0,0)
    score = search(i, 32, resources, bots)
    search.cache_clear()
    blueprint_scores.append(score)

print(reduce(operator.mul, blueprint_scores, 1))