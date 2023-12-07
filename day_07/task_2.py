from collections import Counter

with open("day_07/input.txt") as f:
    lines = f.readlines()

relative_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
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

list_of_games = []
for line in lines:
    # Parse input
    line = line.strip()
    cards_in_hand, bid = line.split(" ")
    counter = Counter(cards_in_hand)
    J_number = counter.pop("J", 0)

    strength = None
    freq = list(counter.values())
    if freq:
        freq.sort()
        freq[-1] += J_number
    else:
        freq = [J_number]
    for key, value in rules.items():
        if value == freq:
            strength = key
            break

    value = 0
    for card in cards_in_hand:
        value = value * 20 + relative_strength[card]

    ultimate_strength = strength * pow(20, 8) + value
    list_of_games.append((ultimate_strength, int(bid)))

# sorting by strength
list_of_games.sort(key=lambda x: x[0])

sum = 0
for rank, (_, bid) in enumerate(list_of_games, start=1):
    sum += bid * rank

print(sum)
