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
    def __init__(self, value, neighbors, x, y):
        self.value = value
        self.neighbors = neighbors
        self.x = x
        self.y = y
        self.direction = 0

    def __repr__(self):
        return f"Node({self.value})"


graph = []
for row in maze:
    row_graph = []
    for i, cell in enumerate(row):
        row_graph.append(Node(cell, [], i, len(graph)))

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

list_of_nodes = [prev_node, current_node]

while current_node.value != "S":
    if current_node.value == "|":
        current_node.direction = prev_node.y - current_node.y
    elif current_node.value in ["7", "F"]:
        if current_node.y - prev_node.y == -1:
            current_node.direction = 1
        elif current_node.y - prev_node.y == 0:
            current_node.direction = -1

    for neighbor in current_node.neighbors:
        if neighbor is not prev_node:
            prev_node = current_node
            current_node = neighbor
            break
    list_of_nodes.append(current_node)

counter = 0
for row in graph:
    for i, node in enumerate(row):
        if node in list_of_nodes:
            continue
        left = 0
        for lefts in row[:i]:
            left += lefts.direction
        if left in [-1, 1]:
            counter += 1
print(counter)
