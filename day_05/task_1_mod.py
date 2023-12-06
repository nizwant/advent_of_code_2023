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
        i = [int(num) for num in i.split()]
        maps[-1].append([i[0] - i[1], i[1], i[1] + i[2]])

for i, map in enumerate(maps):
    map.sort(key=lambda x: x[1])
    maps[i] = map


minimum = float("inf")
for seed in seeds:
    key = seed
    for map in maps:
        low, high = 0, len(map) - 1
        result_index = -1

        while low <= high:
            mid = (low + high) // 2

            if map[mid][1] <= key:
                result_index = mid
                low = mid + 1
            else:
                high = mid - 1

        if key < map[result_index][2] and key >= map[result_index][1]:
            key += map[result_index][0]

    if key < minimum:
        minimum = key


print(minimum)
