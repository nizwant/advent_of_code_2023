with open("day_11/input.txt", "r") as input_file:
    data = input_file.readlines()

data = [list(line.strip()) for line in data]
data_with_expanded_rows = []
for row in data:
    data_with_expanded_rows.append(row)
    if "#" not in row:
        data_with_expanded_rows.append(row)

transposed_data_with_expanded_rows = list(zip(*data_with_expanded_rows))
expanded_data_transposed = []
for row in transposed_data_with_expanded_rows:
    expanded_data_transposed.append(row)
    if "#" not in row:
        expanded_data_transposed.append(row)

expanded_data = list(zip(*expanded_data_transposed))

list_of_galaxies = []
for i, row in enumerate(expanded_data):
    for j, cell in enumerate(row):
        if cell == "#":
            list_of_galaxies.append((i, j))

accumulator = 0
for i, first in enumerate(list_of_galaxies):
    for j, second in enumerate(list_of_galaxies):
        if i > j:
            continue
        accumulator += abs(first[0] - second[0]) + abs(first[1] - second[1])

print(accumulator)
