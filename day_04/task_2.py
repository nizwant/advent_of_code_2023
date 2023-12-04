with open("./day_04/input.txt") as f:
    lines = f.readlines()

cards = [1 for _ in range(len(lines))]
for it, line in enumerate(lines):
    numbers = line.strip().split(": ")[1].split(" | ")
    winning_numbers = numbers[0].split()
    my_numbers = numbers[1].split()

    counter = 0
    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            counter += 1

    for i in range(counter):
        cards[it + i + 1] += cards[it]

print(sum(cards))
