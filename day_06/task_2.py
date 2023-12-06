with open("day_06/input.txt") as f:
    data = f.readlines()

tmp = []
for i in data:
    tmp.append("".join(i.split(":")[1].strip().split()))


data = [[int(tmp[0]), int(tmp[1])]]

mult = 1
for time, record in data:
    print(time, record)
    counter = 0
    for charging in range(time):
        if charging * (time - charging) >= record:
            counter += 1

    mult *= counter
print(mult)
