def process_game_line(line):
    game_parts = line.split('; ')
    game_data = []

    for part in game_parts:
        colors = {'red': 0, 'green': 0, 'blue': 0}
        color_data = part.split(', ')

        for item in color_data:
            number, color = item.split()
            colors[color] = int(number)

        game_data.append(tuple(colors.values()))

    return game_data


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    game_dict = {}

    for line in lines:
        if line.startswith('Game'):
            game_number = int(line.split(':')[0].split()[1])
            game_data = process_game_line(line.split(':')[1].strip())
            game_dict[game_number] = game_data

    return game_dict


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
game_dict = read_input_file(file_path)
print(check_game(game_dict))