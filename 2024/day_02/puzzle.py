from utils.debugging import PrintDebug
import copy


class Puzzle:
    _file_name: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self._file_name = file_name
        self._puzzle_part = puzzle_part
        self._debug = PrintDebug(debug_level)
        self._debug_level = debug_level
        self._level_data = []
        self._distances = []
        self._safe = 0
        self._unsafe_data = []

    def print_run_info(self):
        self._debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self._puzzle_part} with file "
                            f"{self._file_name} and debug level {self._debug_level}")

    def print(self):
        pass

    def parse(self):
        with open(self._file_name) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip().split()
                    level = [int(x) for x in line]
                    distance = [level[y] - level[y-1] for y in range(1, len(level))]
                    self._debug.print(2, f"level is {level} ; distance is {distance}")
                    self._level_data.append(level)
                    self._distances.append(distance)
                    self._debug.increase_indent()
                    if (len([x for x in distance if x > 0]) == len(distance)) \
                            or (len([x for x in distance if x < 0]) == len(distance)):
                        self._debug.print(3, "all increasing or decreasing")
                        if len([x for x in distance if (x > 3 or x < -3)]) == 0:
                            self._debug.print(3, "all increasing gently")
                            self._safe += 1
                        else:
                            self._unsafe_data.append(level)
                    else:
                        self._unsafe_data.append(level)
                    self._debug.decrease_indent()
                else:
                    pass

    def reprocess_data(self):
        for new_level in self._unsafe_data:
            self._debug.print(2, f"reprocess level is {new_level}")
            for x, item in enumerate(new_level):
                my_level = copy.deepcopy(new_level)
                my_level.pop(x)
                if self.check_safety(my_level):
                    self._safe += 1
                    break

    def check_safety(self, level_data):
        my_level_data = level_data
        self._debug.increase_indent()
        self._debug.print(3, f"checking safety of  {my_level_data}")
        distance = [my_level_data[y] - my_level_data[y - 1] for y in range(1, len(my_level_data))]
        if (len([x for x in distance if x > 0]) == len(distance)) or \
                (len([x for x in distance if x < 0]) == len(distance)):
            self._debug.increase_indent()
            self._debug.print(4, f"all increasing or decreasing")
            if len([x for x in distance if (x > 3 or x < -3)]) == 0:
                self._debug.print(4, "all increasing gently")
                self._debug.decrease_indent()
                self._debug.decrease_indent()
                return True
            else:
                self._debug.decrease_indent()
                self._debug.decrease_indent()
                return False
        self._debug.decrease_indent()

    def solve(self):
        self._debug.set_debug_level(1)
        self.print_run_info()
        self.parse()
        self.print()
        if self._puzzle_part == "a":
            self._debug.print(5, f"unsafe levels are {len(self._unsafe_data)}")
            return self._safe
        else:
            self._debug.print(5, f"unsafe data is {self._unsafe_data}")
            self._debug.print(5, f"unsafe levels are {len(self._unsafe_data)}")
            self.reprocess_data()
            return self._safe
