from utils.debugging import PrintDebug
import re


class EngineMap:
    def __init__(self, puzzle_part, debug_context):
        self.puzzle_part = puzzle_part
        self.debug = debug_context
        self.engine_map = []
        self.adjacency_map = {}
        self.symbol_map = []
        self.parts_value = 0
        self.parts = set()

    def add_line(self, line):
        self.debug.print(3, f"adding line: {line}")
        self.engine_map.append([*line])
        current_line_no = len(self.engine_map) - 1
        self.debug.increase_indent()
        self.debug.print(3, f"current line number is: {current_line_no}")
        numbers_in_line = re.findall('\d+', line)
        self.debug.print(3, f"found numbers {numbers_in_line}")
        self.debug.decrease_indent()
        for number in numbers_in_line:
            for location in [m.start() for m in re.finditer(number, line)]:
                self.adjacency_map[(number, current_line_no, location)] = []
                self.adjacency_map[(number, current_line_no, location)].append([current_line_no, location - 1])
                self.adjacency_map[(number, current_line_no, location)].append(
                    [current_line_no, location + len(number)])
                for i in range(location - 1, location + len(number) + 1):
                    self.adjacency_map[(number, current_line_no, location)].append([current_line_no - 1, i])
                    self.adjacency_map[(number, current_line_no, location)].append([current_line_no + 1, i])
            self.debug.print(3,
                             f"adjacency map for {number} is {self.adjacency_map[(number, current_line_no, location)]}")
        for symbol in [m.start() for m in re.finditer('[^\d.]', line)]:
            self.symbol_map.append([current_line_no, symbol])

    def find_parts(self):
        for i in self.symbol_map:
            self.debug.print(2, f"finding matches for symbol at {i}")
            for val_tuple, adjacent_coordinates in self.adjacency_map.items():
                if i in adjacent_coordinates:
                    self.debug.print(2, f"adding value of {val_tuple} to total")
                    self.parts_value += int(val_tuple[0])
                    self.parts.add(val_tuple)
        self.debug.print(2, f"parts:  {self.parts}")
        self.parts_value = sum([int(_x[0]) for _x in self.parts])
        return self.parts_value


    def print_map(self):
        self.debug.print(2, f"Current Engine Map:")
        self.debug.increase_indent()
        for index, i in enumerate(self.engine_map):
            self.debug.print(2, f"{index: 3} {i}")
        self.debug.decrease_indent()


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.my_engine_map = EngineMap(puzzle_part, self.debug)

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        self.my_engine_map.print_map()

    def parse(self):

        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    self.my_engine_map.add_line(line)
                else:
                    pass

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.my_engine_map.find_parts()
        else:
            return 0
