from functools import reduce
import math

with open("day_08/input.txt") as f:
    data = f.readlines()

directions = list(data[0].strip())

graph = {}
for i in data[2:]:
    node, edges = i.strip().split(" = ")
    graph[node] = [edges[1:4], edges[6:9]]


starting_nodes = [i for i in graph.keys() if i[2:] == "A"]
counters = [0] * len(starting_nodes)
# visited = [False] * len(starting_nodes)

for i, node in enumerate(starting_nodes):
    current_node = node
    while current_node[2:] != "Z":  # or not visited[i]:
        # if current_node[2:] == "Z":
        #     visited[i] = True

        if directions[counters[i] % len(directions)] == "L":
            current_node = graph[current_node][0]
        else:
            current_node = graph[current_node][1]
        counters[i] += 1

# its looping so I need to find smallest common multiple of counters
smc = lambda x, y: abs(x * y) // math.gcd(x, y)
print(reduce(smc, counters))
