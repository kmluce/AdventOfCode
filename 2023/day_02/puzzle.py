from utils.debugging import PrintDebug
from operator import mul
from functools import reduce


class CubeGame:
    def __init__(self, game_params, debug_contex, puzzle_part):
        self.game_parameters = game_params
        self.game_data = []
        self.debug = debug_contex
        self.color_index = {'red': 0, 'green': 1, 'blue': 2}
        self.total_valid = 0
        self.puzzle_part = puzzle_part

    def add_game(self, line):
        self.game_data.append(line)
        first_parse = line.split(':')
        game_index = int(first_parse[0].replace("Game ", ""))
        self.debug.print(2, f"Game # {game_index}")
        game_tries = first_parse[1].split(';')
        self.debug.print(2, f"  Game tries: {game_tries}")
        game_valid = True
        max_cubes = [0, 0, 0]
        for game_try in game_tries:
            for dice_show in game_try.split(','):
                for color in self.color_index.keys():
                    if color in dice_show:
                        if self.puzzle_part == 'a':
                            if int(dice_show.strip().split()[0]) > self.game_parameters[self.color_index[color]]:
                                game_valid = False
                                break
                        else:
                            if int(dice_show.strip().split()[0]) > max_cubes[self.color_index[color]]:
                                max_cubes[self.color_index[color]] = int(dice_show.strip().split()[0])
        if self.puzzle_part == 'a':
            if game_valid:
                self.total_valid += game_index
        else:
            self.debug.print(2, f"max_cubes is: {max_cubes}")
            self.total_valid += reduce(mul, max_cubes)

    def get_total(self):
        return self.total_valid


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    def parse(self, cube_game):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    cube_game.add_game(line)
                else:
                    pass

    def solve(self):
        self.print()
        if self.puzzle_part == "a":
            cube_game = CubeGame([12, 13, 14], self.debug, self.puzzle_part)
            self.parse(cube_game)
            return cube_game.get_total()
        else:
            cube_game = CubeGame([12, 13, 14], self.debug, self.puzzle_part)
            self.parse(cube_game)
            return cube_game.get_total()
