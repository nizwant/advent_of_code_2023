from collections import Counter

with open("day_07/input.txt") as f:
    lines = f.readlines()

relative_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

rules = {
    1: [1, 1, 1, 1, 1],
    2: [1, 1, 1, 2],
    3: [1, 2, 2],
    4: [1, 1, 3],
    5: [2, 3],
    6: [1, 4],
    7: [
        5,
    ],
}

# Parse input
data = []
for line in lines:
    line = line.strip()
    cards = line.split(" ")
    counter = Counter(cards[0])

    strength = None
    freq = list(counter.values())
    freq.sort()
    for key, value in rules.items():
        if value == freq:
            strength = key
            break

    value = 0
    for i in cards[0]:
        value = value * 20 + relative_strength[i]

    ultimate_strength = strength * pow(20, 8) + value
    data.append((ultimate_strength, int(cards[1])))

data.sort(key=lambda x: x[0])
for i in data:
    print(i)
sum = 0
for i, game in enumerate(data, start=1):
    sum += game[1] * i

print(sum)
# 252507641
# 247032777
