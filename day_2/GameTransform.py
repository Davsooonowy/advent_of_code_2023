class GameTransform:
    def __init__(self, file_path):
        self.file_path = file_path
        self.game_dict = self._read_input_file()

    def _process_game_line(self, line):
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

    def _read_input_file(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        game_dict = {}

        for line in lines:
            if line.startswith('Game'):
                game_number = int(line.split(':')[0].split()[1])
                game_data = self._process_game_line(line.split(':')[1].strip())
                game_dict[game_number] = game_data

        return game_dict

    def get_game_dict(self):
        return self.game_dict