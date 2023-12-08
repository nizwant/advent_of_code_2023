with open("day_08/input.txt") as f:
    data = f.readlines()

directions = list(data[0].strip())

graph = {}
for i in data[2:]:
    node, edges = i.strip().split(" = ")
    graph[node] = [edges[1:4], edges[6:9]]

counter = 0
current_node = "AAA"
while current_node != "ZZZ":
    if directions[counter % len(directions)] == "L":
        current_node = graph[current_node][0]
    else:
        current_node = graph[current_node][1]
    counter += 1

print(counter)
