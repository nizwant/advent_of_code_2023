with open("day_14/input.txt", "r") as f:
    data = f.readlines()

# creating a platform
platform = []
for i, row in enumerate(data):
    row = row.strip()
    platform.append(list(row))


# north rotation
def north(platform):
    next_rock_y = [0 for _ in data[0]]
    for i, row in enumerate(platform):
        for j, cell in enumerate(row):
            if cell == "O":
                platform[i][j] = "."
                platform[next_rock_y[j]][j] = "O"
                next_rock_y[j] += 1
            elif cell == "#":
                next_rock_y[j] = i + 1
    return platform


def south(platform):
    platform = platform[::-1]
    platform = north(platform)
    platform = platform[::-1]
    return platform


def west(platform):
    platform = list(zip(*platform))
    platform = [list(row) for row in platform]
    platform = north(platform)
    platform = list(zip(*platform))
    platform = [list(row) for row in platform]
    return platform


def east(platform):
    platform = list(zip(*platform))
    platform = [list(row) for row in platform]
    platform = south(platform)
    platform = list(zip(*platform))
    platform = [list(row) for row in platform]
    return platform


loads_after_rotations = []
# i assume that after 1000 rotations the platform will begin to repeat
for i in range(1, 1_000):  # 1_000_000_000
    platform = north(platform)
    platform = west(platform)
    platform = south(platform)
    platform = east(platform)

    # calculating the load on north beams
    acc = 0
    weight = len(platform)
    for row in platform:
        for cell in row:
            if cell == "O":
                acc += weight
        weight -= 1
    loads_after_rotations.append((i, acc))

# and that max length of cycle is 100
# it is not ideal but it works
for length_of_cycle in range(2, 100):
    set_of_loads = set()
    for i, load in loads_after_rotations[-length_of_cycle:]:
        set_of_loads.add((i % length_of_cycle, load))

    set_of_loads_2 = set()
    for i, load in loads_after_rotations[-2 * length_of_cycle :]:
        set_of_loads_2.add((i % length_of_cycle, load))

    if set_of_loads == set_of_loads_2:
        for i, val in set_of_loads:
            if i == 1_000_000_000 % length_of_cycle:
                print(val)
        break
