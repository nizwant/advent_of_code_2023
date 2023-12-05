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
        i = [int(num) for num in i.split()]
        maps[-1].append([i[0] - i[1], i[1], i[1] + i[2]])

for i, map in enumerate(maps):
    map.sort(key=lambda x: x[1])
    maps[i] = map

i = 0
minimum = float("inf")
for seed_start, seed_num in seeds:
    for seed in range(seed_start, seed_start + seed_num):
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
        print(i)
        i += 1

print(minimum)
