with open("day_08/input.txt") as f:
    data = f.readlines()

directions = list(data[0].strip())

graph = {}
for i in data[2:]:
    node, edges = i.strip().split(" = ")
    graph[node] = [edges[1:4], edges[6:9]]

counter = 0
current_node = [i for i in graph.keys() if i[2:] == "A"]
while all([node[2:] != "Z"] for node in current_node):
    if directions[counter % len(directions)] == "L":
        for i in range(len(current_node)):
            current_node[i] = graph[current_node[i]][0]
    else:
        for i in range(len(current_node)):
            current_node[i] = graph[current_node[i]][1]
    counter += 1

print(counter)
