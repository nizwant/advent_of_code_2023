# read input
with open("input.txt") as f:
    data = f.readlines()

accumulator = 0
for line in data:
    list_of_numbers = list(filter(lambda x: x in "0123456789", line))
    number = int(list_of_numbers[0] + list_of_numbers[-1])
    accumulator += number

print(accumulator)
