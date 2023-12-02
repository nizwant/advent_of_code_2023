with open("input.txt") as f:
    data = f.readlines()

dict_of_game = {"red": 12, "green": 13, "blue": 14}

sum_of_id_of_valid_games = 0
for id, line in enumerate(data, 1):
    line = line.strip().split(": ")
    game_state = line[1].replace(";", ",")
    game_state = game_state.split(", ")
    valid_game = True
    for round in game_state:
        round = round.split(" ")
        color = round[1]
        quantity = int(round[0])
        if quantity > dict_of_game[color]:
            valid_game = False
            break

    if valid_game:
        sum_of_id_of_valid_games += id

print(sum_of_id_of_valid_games)
