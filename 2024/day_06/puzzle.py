from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.local_map = []
        self.count_x = 0

    def print_run_info(self):
        self.debug.print(1, "")
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        self.debug.print(2, "current map is:")
        self.debug.increase_indent()
        for line in self.local_map:
            self.debug.print(2, f"{line}")
        self.debug.decrease_indent()
        pass

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    self.local_map.append(list(line))
                else:
                    pass

    def walk_map(self):
        starting_location = []
        direction = [-1, 0]
        # -1, 0
        #  0, 1
        #  1, 0
        #  0, -1
        for index, row in enumerate(self.local_map):
            if '^' in row:
                starting_location = [index, row.index('^')]
        current_location = starting_location
        while (-1 < current_location[0] < len(self.local_map)
               and -1 < current_location[1] < len(self.local_map[0])):
            self.local_map[current_location[0]][current_location[1]] = 'X'
            self.print()
            if current_location[0] + direction[0] < 0 or current_location[0] + direction[0] >= len(self.local_map):
                break
            elif current_location[1] + direction[1] < 0 or current_location[0] + direction[1] >= len(self.local_map[0]):
                break
            elif self.local_map[current_location[0] + direction[0]][current_location[1] + direction[1]] == '#':
                if direction == [-1, 0]:
                    direction = [0, 1]
                elif direction == [0, 1]:
                    direction = [1, 0]
                elif direction == [1, 0]:
                    direction = [0, -1]
                else:
                    direction = [-1, 0]
            current_location[0] += direction[0]
            current_location[1] += direction[1]
        for line in self.local_map:
            self.count_x += len([x for x in line if x == 'X'])

    def solve(self):
        self.print_run_info()
        self.parse()
        self.print()
        self.walk_map()
        self.print()
        if self.puzzle_part == "a":
            return self.count_x
        else:
            return 0
