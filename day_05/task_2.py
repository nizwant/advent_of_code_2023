with open("./day_05/input.txt", "r") as f:
    data = f.readlines()

seed_row = data[0].strip().split(": ")[1].split()
seeds = [(int(i), int(j)) for i, j in zip(seed_row[::2], seed_row[1::2])]


maps = []
for i in data[2:]:
    i = i.strip()
    if ":" in i:
        maps.append([])
    elif i == "":
        continue
    else:
        maps[-1].append([int(num) for num in i.split()])

minimum = float("inf")
for seed_start, seed_num in seeds:
    ran = range(seed_start, seed_start + seed_num)
    for seed in ran:
        key = seed
        for map in maps:
            for mapper in map:
                if key >= mapper[1] and key < mapper[1] + mapper[2]:
                    key = mapper[0] + key - mapper[1]
                    break

        if key < minimum:
            minimum = key


print(minimum)
