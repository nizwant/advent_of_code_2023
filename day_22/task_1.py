with open("day_22/input.txt", "r") as f:
    data = []
    for i, line in enumerate(f):
        line = line.strip()
        line = line.split("~")

        start = line[0].split(",")
        end = line[1].split(",")
        start = [int(s) for s in start]
        end = [int(e) for e in end]

        data.append((start, end))

data.sort(key=lambda x: int(x[0][2]))

# grid in xy plane
max_x = max(data, key=lambda x: x[1][0])[1][0]
min_x = min(data, key=lambda x: x[0][0])[0][0]
max_y = max(data, key=lambda x: x[1][1])[1][1]
min_y = min(data, key=lambda x: x[0][1])[0][1]
levels = [[1 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

for i, (start, end) in enumerate(data):
    max_hight = 0
    counter = 0
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if levels[y][x] > max_hight:
                max_hight = levels[y][x]
                counter = 0
            if levels[y][x] == max_hight:
                counter += 1

    height_diff = start[2] - max_hight
    data[i][0][2] = max_hight
    data[i][1][2] = data[i][1][2] - height_diff

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            levels[y][x] = data[i][1][2] + 1

answer = 0
for i, (start, end) in enumerate(data):
    list_of_blocks_directly_above = []
    set_of_blocks_directly_above = set()
    for s, e in data:
        if s[2] == start[2] + 1:
            list_of_blocks_directly_above.append((s, e))
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for s, e in list_of_blocks_directly_above:
                if s[0] <= x <= e[0] and s[1] <= y <= e[1]:
                    set_of_blocks_directly_above.add((s, e))
    if len(set_of_blocks_directly_above) == 0:
        pass

print(answer)
