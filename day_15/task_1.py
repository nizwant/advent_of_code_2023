with open("day_15/input.txt", "r") as file:
    line = file.readline()

line = line.strip().split(",")

accumulator = 0
for instruction in line:
    num = 0
    for char in instruction:
        num += ord(char)
        num *= 17
        num %= 256
    accumulator += num

print(accumulator)
