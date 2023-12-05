with open("./day_05/input.txt", "r") as f:
    data = f.readlines()

seeds = [int(i) for i in data[0].strip().split(": ")[1].split()]

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
for seed in seeds:
    key = seed
    for map in maps:
        for mapper in map:
            if key >= mapper[1] and key < mapper[1] + mapper[2]:
                key = mapper[0] + key - mapper[1]
                break

    if key < minimum:
        minimum = key


print(minimum)
