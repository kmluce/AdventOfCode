from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.total_num = 0

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    @staticmethod
    def findall(p, s):
        i = s.find(p)
        while i != -1:
            yield i
            i = s.find(p, i + 1)

    def find_numbers_in_string(self, line):
        numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                   'eight': '8', 'nine': '9'}
        positions = []
        for i in numbers.keys():
            positions.extend([(x, numbers[i]) for x in self.findall(i, line)])
        positions.extend([(ind, s) for ind, s in enumerate(list(line)) if s.isdigit()])
        positions.sort()
        return [i[1] for i in positions]

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    if self.puzzle_part == 'b':
                        calibration_numbers = self.find_numbers_in_string(line)
                    else:
                        calibration_numbers = [s for s in list(line) if s.isdigit()]
                    self.total_num += int(calibration_numbers[0] + calibration_numbers[-1])
                else:
                    pass

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.total_num
        else:
            return self.total_num
