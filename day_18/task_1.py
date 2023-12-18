with open("day_18/input.txt", "r") as f:
    data = f.readlines()

data = [line.strip().split() for line in data]
modified_data = []

x, y = 0, 0
min_x, min_y = 0, 0
max_x, max_y = 0, 0
for row in data:
    for _ in range(int(row[1])):
        modified_data.append((x, y, row[2]))
        if row[0] == "R":
            x += 1
            max_x = max(max_x, x)
        elif row[0] == "L":
            x -= 1
            min_x = min(min_x, x)
        elif row[0] == "U":
            y += 1
            max_y = max(max_y, y)
        elif row[0] == "D":
            y -= 1
            min_y = min(min_y, y)

grid = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
for row in modified_data:
    x, y = row[0] - min_x, row[1] - min_y
    grid[y][x] = 1

que = [((max_x - min_x) // 2, (max_y - min_y) // 2)]
while que:
    x, y = que.pop(0)
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 1:
        continue
    if grid[y][x] == 0:
        grid[y][x] = 1
        que.append((x + 1, y))
        que.append((x - 1, y))
        que.append((x, y + 1))
        que.append((x, y - 1))

answer = 0
for row in grid:
    answer += sum(row)

print(answer)
