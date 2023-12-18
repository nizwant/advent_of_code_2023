with open("day_18/input.txt", "r") as f:
    data = f.readlines()

data = [line.strip().split() for line in data]
modified_data = []

x, y = 0, 0
min_x, min_y = 0, 0
max_x, max_y = 0, 0
aaa = 0

for row in data:
    old_x, old_y = x, y
    aaa += int(row[1])
    if row[0] == "R":
        x += int(row[1])
        max_x = max(max_x, x)
    elif row[0] == "L":
        x -= int(row[1])
        min_x = min(min_x, x)
    elif row[0] == "U":
        y += int(row[1])
        max_y = max(max_y, y)
    elif row[0] == "D":
        y -= int(row[1])
        min_y = min(min_y, y)
    modified_data.append((old_x, old_y, x, y))


answer = 0
for row in modified_data:
    answer += (row[0] - row[2]) * (row[1] + row[3])

answer = abs(answer - aaa) // 2 + 1

print(answer)
