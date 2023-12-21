data = []
with open("day_21/input2.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            start = (line.index("S"), i)
            line = line.replace("S", ".")
        data.append(list(line))

import time

start_time = time.time()

visited_positions = set([start])
counter_odd = 1
counter_even = 0

possible_positions = [start]
for i in range(2000):
    unvisited_positions_in_next_step = []
    for x, y in possible_positions:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) in visited_positions:
                continue
            if data[(new_y) % len(data)][(new_x) % len(data[0])] == ".":
                unvisited_positions_in_next_step.append((new_x, new_y))
                visited_positions.add((new_x, new_y))
                if i % 2 == 0:
                    counter_even += 1
                else:
                    counter_odd += 1

    possible_positions = unvisited_positions_in_next_step


print(time.time() - start_time)

if i % 2 == 0:
    print(counter_odd)
else:
    print(counter_odd)
