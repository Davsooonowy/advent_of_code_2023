from day_1.ex2.GameTransform import GameTransform


def check_game(game_data):
    sum_of_power = 0
    for game_number, game_result in game_data.items():
        min_red, min_green, min_blue = map(max, zip(*game_result))
        sum_of_power += min_red * min_green * min_blue
    return sum_of_power


file_path = 'input.txt'
transformer = GameTransform(file_path)
game_dict = transformer.get_game_dict()
print(check_game(game_dict))
