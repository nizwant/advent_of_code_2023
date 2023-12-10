with open("day_10/input.txt", "r") as f:
    data = f.readlines()

maze = [list(line.strip()) for line in data]

moves = {
    "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "L": [(-1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    ".": [],
}


class Node:
    def __init__(self, value, neighbors):
        self.value = value
        self.neighbors = neighbors

    def __repr__(self):
        return f"Node({self.value})"


graph = []
for row in maze:
    row_graph = []
    for i, cell in enumerate(row):
        row_graph.append(Node(cell, []))

    graph.append(row_graph)

for i, row in enumerate(graph):
    for j, node in enumerate(row):
        for move in moves[node.value]:
            try:
                node.neighbors.append(graph[i + move[0]][j + move[1]])
            except IndexError:
                pass

start = None
for row in graph:
    for node in row:
        if node.value == "S":
            start = node
            break
    if start:
        break

prev_node = current_node = start
for neighbor in current_node.neighbors:
    if start in neighbor.neighbors:
        current_node = neighbor
        break

counter = 1
while current_node.value != "S":
    counter += 1
    for neighbor in current_node.neighbors:
        if neighbor is not prev_node:
            prev_node = current_node
            current_node = neighbor
            break

print(counter // 2)
