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

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    print('line:', line)
                    if self.puzzle_part == 'b':
                        line.replace('one', '1')
                        line.replace('two', '2')
                        line.replace('three', '3')
                        line.replace('four', '4')
                        line.replace('five', '5')
                        line.replace('six', '6')
                        line.replace('seven', '7')
                        line.replace('eight', '8')
                        line.replace('nine', '9')
                    print('line after replacement:', line)
                    calibration_numbers = [s for s in list(line) if s.isdigit()]
                    print('calibration numbers:', calibration_numbers)
                    print('adding these:', int(calibration_numbers[0] + calibration_numbers[-1]))
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
