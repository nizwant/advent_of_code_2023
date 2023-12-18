with open("day_18/input.txt", "r") as f:
    data = f.readlines()

data = [line.strip().split("#")[1] for line in data]
data = [line.strip(")") for line in data]
modified_data = []

x, y = 0, 0
min_x, min_y = 0, 0
max_x, max_y = 0, 0

aaa = 0
for row in data:
    length = int(row[:-1], 16)
    olx_x, old_y = x, y
    aaa += length
    if row[-1] == "0":
        x += length
        max_x = max(max_x, x)
    elif row[-1] == "2":
        x -= length
        min_x = min(min_x, x)
    elif row[-1] == "3":
        y += length
        max_y = max(max_y, y)
    elif row[-1] == "1":
        y -= length
        min_y = min(min_y, y)
    modified_data.append((olx_x, old_y, x, y))
modified_data.append((x, y, 0, 0))

answer = 0
for row in modified_data:
    answer += (row[0] - row[2]) * (row[1] + row[3])

answer = abs(answer - aaa) // 2 + 1

print(answer)
