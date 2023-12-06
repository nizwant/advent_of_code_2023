with open("day_06/input.txt") as f:
    data = f.readlines()

tmp = []
for i in data:
    tmp.append(i.split(":")[1].strip().split())

data = []
for i, j in zip(tmp[0], tmp[1]):
    data.append([int(i), int(j)])

mult = 1
for time, record in data:
    counter = 0
    for charging in range(time):
        if charging * (time - charging) >= record:
            counter += 1

    mult *= counter
print(mult)
