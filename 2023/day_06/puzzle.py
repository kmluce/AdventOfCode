from utils.debugging import PrintDebug
import math


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.times = []
        self.distances = []

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    @staticmethod
    def real_quadratic(a, b, c):
        discriminate = b * b - 4 * a * c
        square_root_val = math.sqrt(abs(discriminate))
        if discriminate > 0:
            return [(-b + square_root_val) / (2 * a), (-b - square_root_val) / (2 * a)]
        elif discriminate == 0:
            return [(-b / (2 * a))]

    def get_race_solutions(self, time, distance):
        lower_bound, upper_bound = self.real_quadratic(-1, time, distance * -1)
        print(
            f"got solutions {lower_bound}, {upper_bound} from race with time {time} and distance {distance}")
        upper_floor = math.floor(upper_bound)
        lower_floor = math.floor(lower_bound)
        if lower_floor == lower_bound:
            lower_floor += 1
        return upper_floor - lower_floor

    def record_factor(self):
        total_record = 1
        for index, time in enumerate(self.times):
            total_record *= self.get_race_solutions(time, self.distances[index])
        return total_record

    def cat_int_list(self, list_of_ints):
        int_string = ""
        for item in list_of_ints:
            int_string = int_string + str(item)
        return int(int_string)

    def record_single_race(self):
        return self.get_race_solutions(self.cat_int_list(self.times), self.cat_int_list(self.distances))

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    if line.startswith("Time:"):
                        self.times = [int(x) for x in line.split()[1:]]
                    elif line.startswith("Distance:"):
                        self.distances = [int(x) for x in line.split()[1:]]
                else:
                    pass

    def solve(self):
        self.print()
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.record_factor()
        else:
            return self.record_single_race()
