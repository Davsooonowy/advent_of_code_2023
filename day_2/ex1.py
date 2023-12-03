from day_2.GameTransform import GameTransform


def check_game(game_data):
    red, green, blue, sum_of_id = 12, 13, 14, 0
    for game_number, game_result in game_data.items():
        flag = False
        for i in range(len(game_result)):
            if game_result[i][0] > red or game_result[i][1] > green or game_result[i][2] > blue:
                flag = True
                break
        if not flag:
            sum_of_id += game_number
    return sum_of_id


file_path = 'input.txt'
transformer = GameTransform(file_path)
game_dict = transformer.get_game_dict()
print(check_game(game_dict))