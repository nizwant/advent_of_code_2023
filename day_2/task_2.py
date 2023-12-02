with open("input.txt") as f:
    data = f.readlines()


sum_power = 0
for line in data:
    line = line.strip().split(": ")
    game_state = line[1].replace(";", ",")
    game_state = game_state.split(", ")
    dict_of_game = {"red": 0, "green": 0, "blue": 0}
    for round in game_state:
        round = round.split(" ")
        color = round[1]
        quantity = int(round[0])
        dict_of_game[color] = max(dict_of_game[color], quantity)

    sum_power += dict_of_game["red"] * dict_of_game["green"] * dict_of_game["blue"]

print(sum_power)
