with open("day_15/input.txt", "r") as file:
    line = file.readline()

line = line.strip().split(",")

boxes = [[] for _ in range(256)]
for instruction in line:
    box_number = 0

    if instruction[-1] == "-":
        for char in instruction[:-1]:
            box_number += ord(char)
            box_number *= 17
            box_number %= 256
        for lens in boxes[box_number]:
            if instruction[:-1] == lens[:-2]:
                boxes[box_number].remove(lens)
                break
    else:
        for char in instruction[:-2]:
            box_number += ord(char)
            box_number *= 17
            box_number %= 256
        for i, lens in enumerate(boxes[box_number]):
            if instruction[:-2] == lens[:-2]:
                boxes[box_number][i] = instruction
                break
        else:
            boxes[box_number].append(instruction)

acc = 0
for i, box in enumerate(boxes, 1):
    for j, lens in enumerate(box, 1):
        acc += int(lens[-1]) * i * j

print(acc)
