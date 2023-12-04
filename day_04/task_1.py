with open("./day_04/input.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    numbers = line.strip().split(": ")[1].split(" | ")
    winning_numbers = numbers[0].split()
    my_numbers = numbers[1].split()

    counter = 0
    for number in winning_numbers:
        if number in my_numbers:
            counter += 1

    if counter == 0:
        pass
    else:
        sum += 2 ** (counter - 1)

print(sum)
