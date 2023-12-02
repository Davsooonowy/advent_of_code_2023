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
    sum_of_power = 0
    for game_number, game_result in game_data.items():
        min_red, min_green, min_blue = map(max, zip(*game_result))
        sum_of_power += min_red * min_green * min_blue
    return sum_of_power


file_path = 'input.txt'
game_dict = read_input_file(file_path)
print(check_game(game_dict))