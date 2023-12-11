with open("day_11/input.txt", "r") as input_file:
    data = input_file.readlines()

data = [list(line.strip()) for line in data]
rows_to_expand = []
for i, row in enumerate(data):
    if "#" not in row:
        rows_to_expand.append(i)

transposed_data = list(zip(*data))
columns_to_expand = []
for j, row in enumerate(transposed_data):
    if "#" not in row:
        columns_to_expand.append(j)

list_of_galaxies = []
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == "#":
            list_of_galaxies.append((i, j))

accumulator = 0
expansion_size = 1000000 - 1
for i, first in enumerate(list_of_galaxies):
    for j, second in enumerate(list_of_galaxies):
        if i > j:
            continue
        counter_x = 0
        counter_y = 0
        for k in columns_to_expand:
            if k > min(first[1], second[1]) and k < max(first[1], second[1]):
                counter_x += 1
        for k in rows_to_expand:
            if k > min(first[0], second[0]) and k < max(first[0], second[0]):
                counter_y += 1
        accumulator += (
            abs(first[0] - second[0])
            + abs(first[1] - second[1])
            + expansion_size * (counter_y + counter_x)
        )

print(accumulator)
