with open("day_14/input.txt", "r") as f:
    data = f.readlines()


# data = [
#     "O....#....",
#     "O.OO#....#",
#     ".....##...",
#     "OO.#O....O",
#     ".O.....O#.",
#     "O.#..O.#.#",
#     "..O..#O..O",
#     ".......O..",
#     "#....###..",
#     "#OO..#....",
# ]

platform = []
next_rock_y = [0 for _ in data[0]]
for i, row in enumerate(data):
    row = row.strip()
    platform.append(list(row))
    for j, cell in enumerate(platform[-1]):
        if cell == "O":
            platform[-1][j] = "."
            platform[next_rock_y[j]][j] = "O"
            next_rock_y[j] += 1
        elif cell == "#":
            next_rock_y[j] = i + 1

acc = 0
weight = len(platform)
for row in platform:
    for cell in row:
        if cell == "O":
            acc += weight
    weight -= 1

print(acc)
