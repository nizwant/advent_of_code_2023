data = []
with open("day_21/input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if "S" in line:
            start = (line.index("S"), i)
            line = line.replace("S", ".")
        data.append(list(line))


possible_positions = [start]
for _ in range(64):
    possible_positions_in_next_step = []
    for x, y in possible_positions:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (
                0 <= x + dx < len(data[0])
                and 0 <= y + dy < len(data)
                and data[y + dy][x + dx] == "."
                and (x + dx, y + dy) not in possible_positions_in_next_step
            ):
                possible_positions_in_next_step.append((x + dx, y + dy))
    possible_positions = possible_positions_in_next_step

print(len(possible_positions))
