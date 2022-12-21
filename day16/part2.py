import os
from collections import deque
from itertools import combinations

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def parse(line):
    line = line.replace(",", "")
    line = line.split(" ")
    name = line[1]
    rate = int(line[4].split("=")[1][:-1])
    neighbors = line[9:]
    return [name, rate, neighbors]

valves = [parse(line) for line in myinput]
rates = {valve[0]: valve[1] for valve in valves}
tunnels = {valve[0]: valve[2] for valve in valves}

def get_valve_distances(source, tunnels, rates):
    dist = {}
    visited = set()
    queue = deque([source])
    dist[source] = 0
    while queue:
        v = queue.popleft()
        visited.add(v)    
        neighbors = tunnels[v]
        for u in neighbors:
            if u in visited:
                continue
            if not u in dist:
                dist[u] = dist[v] + 1
                queue.append(u)
    dist[source] = 1
    for v in rates:
        if rates[v] == 0:
            dist.pop(v)
    return dist

path_scores = {}
def search(path, time, score):
    opened_sum = sum([rates[open_valve] for open_valve in path])
    final = score + (30-time)*opened_sum
    if len(path) == len(graph) or time >= 30:
        path_scores[path] = final
        return final

    current_valve = path[-1]
    best_score = final
    for next_valve in graph[current_valve]:
        if next_valve in path:
            continue
        dist = graph[current_valve][next_valve]
        elapsed_time = dist + 1
        if time + elapsed_time > 30:
            continue
        next_path = path + (next_valve,)
        candidate_score = search(next_path, time + elapsed_time, score + elapsed_time*opened_sum)
        if candidate_score > best_score:
            best_score = candidate_score
    path_scores[path] = final
    return best_score

graph = {}
for valve in tunnels:
    if rates[valve] > 0:
        graph[valve] = get_valve_distances(valve, tunnels, rates)

start = get_valve_distances("AA", tunnels, rates)
best_score = 0
for valve in start:
    time = start[valve] + 1 + 4
    score = search((valve,), time, 0)
    if score > best_score:
        best_score = score

subset_scores = {}
for path in path_scores:
    subset = frozenset(path)
    if subset in subset_scores and subset_scores[subset] > path_scores[path]:
        continue
    subset_scores[subset] = path_scores[path]

best_combo_score = 0
for set1, set2 in combinations(subset_scores.keys(), 2):
    if set1.isdisjoint(set2):
        combo_score = subset_scores[set1] + subset_scores[set2]
        if combo_score > best_combo_score:
            best_combo_score = combo_score
print(best_combo_score)