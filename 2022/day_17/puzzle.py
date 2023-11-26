from utils.debugging import PrintDebug
import numpy as np


class DropMap:

    def __init__(self, initial_x, initial_y, num_rocks=2022, debug_context=None):
        self.size_x = initial_x
        self.size_y = initial_y
        self.map = np.zeros((initial_y, initial_x), np.int8)
        if debug_context is None:
            self.debugContext = PrintDebug(0)
        else:
            self.debugContext = debug_context
        # self.map[3][2] = 1
        self.jet_order = []
        self.rocks = [np.array([1, 1, 1, 1]),
                      np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
                      np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
                      np.array([[1], [1], [1], [1]]),
                      np.array([[1, 1], [1, 1]])]
        self.jet_index = 0
        self.max_height = 0
        self.num_rocks = num_rocks
        # self.num_rocks = 10
        self.current_rock = 0
        self.max_drop = 0
        self.cycle_check_list = []
        self.cycle_begin = 0
        self.cycle_end = 0
        self.cycle_length = 0
        self.each_cycle_adds_height = 0
        self.max_height_differential = []

    def add_jets(self, jets):
        for element in jets:
            self.jet_order.append(element)

    def print(self):
        # print(self.map)
        self.debugContext.print(5, "Map:")
        for i in range(self.map.shape[0] - 1, -1, -1):
            self.debugContext.print(5, ['#' if x == 1 else '.' for x in self.map[i].tolist()])
        self.debugContext.print(5, "")

    def print_rocks(self):
        self.debugContext.print(2, f"Printing set of rocks")
        self.debugContext.increase_indent()
        for i in self.rocks:
            self.debugContext.print(2, f"rock {i} length is {len(i)}")
            self.debugContext.print(2, f"rock {i} shape is {i.shape}")
            self.debugContext.print(2, f"rock {i} is of dimension {i.ndim}")
            self.debugContext.print(2, i)
            self.debugContext.print(2, "")
        self.debugContext.decrease_indent()

    def stringify(self, num_rows=10):
        return np.array2string(self.map[-num_rows:, :]).replace(" ", "")

    def drop_rock(self):
        self.debugContext.print(4, "printing map before padding")
        self.print()
        self.map = np.pad(self.map, [(0, 4), (0, 0)], mode='constant')
        self.debugContext.print(4, "printing map after padding")
        self.print()
        curr_rock_index = self.current_rock % len(self.rocks)
        # curr_rock_index = 1
        self.debugContext.print(4, 'curr rock is:')
        self.debugContext.print(4, self.rocks[curr_rock_index])
        rock_y = self.max_height + 3
        rock_x = 2
        self.print_rock_on_map(curr_rock_index, rock_x, rock_y)

    def drop_rocks(self):
        self.debugContext.print(2, "Starting to Drop Rocks")
        self.debugContext.increase_indent()
        matching_cycle_indexes = []

        for i in range(0, self.num_rocks):
            rock_drop_depth = 0
            self.debugContext.print(2, f"dropping rock {i}")
            self.debugContext.increase_indent()
            curr_rock_index = self.current_rock % len(self.rocks)
            self.debugContext.print(3, f'beginning rock index is is {curr_rock_index}')
            self.debugContext.print(3, f'curr rock is {self.rocks[curr_rock_index]}')
            beginning_jet_index = self.jet_index % len(self.jet_order)
            self.debugContext.print(3, f'beginning jet index is is {beginning_jet_index}')
            rock_width, rock_height = self.get_rock_size(curr_rock_index)
            rock_y = self.max_height + 3
            rock_x = 2
            # define initial state tuple
            drop_initial_state = (curr_rock_index, beginning_jet_index, self.stringify(50))
            self.debugContext.print(3, f"initial state is:  {drop_initial_state}")

            # do any cycles match?
            matching_cycle_indexes = [i for i, x in enumerate(self.cycle_check_list) if x == drop_initial_state]
            self.debugContext.print(3, f"list of matching cycles is {matching_cycle_indexes}")

            if matching_cycle_indexes:
                self.debugContext.print(2, f"breaking out of loop because match detected!")
                self.debugContext.decrease_indent()
                break

            # Save initial state for cycle detection
            self.cycle_check_list.append(drop_initial_state)

            if self.rocks[curr_rock_index].ndim == 1:
                self.map = np.pad(self.map, [(0, 1), (0, 0)], mode='constant')
            else:
                self.map = np.pad(self.map, [(0, len(self.rocks[curr_rock_index])), (0, 0)], mode='constant')
            collision = False
            self.debugContext.print(5, f"printing rock in starting location at {rock_x},{rock_y}")
            self.print_rock_on_map(curr_rock_index, rock_x, rock_y)
            while not collision:
                curr_jet = self.jet_order[self.jet_index % len(self.jet_order)]
                self.debugContext.print(4, f"current jet is {curr_jet}")
                if curr_jet == '>':
                    if self.is_collision(curr_rock_index, rock_x + 1, rock_y):
                        self.debugContext.print(4, f"rock collided on rightward jet")
                    #            collision = True
                    # break
                    else:
                        self.debugContext.print(4, f"rock did NOT collide on rightward jet, adding 1 to x")
                        rock_x = rock_x + 1
                elif curr_jet == '<':
                    if self.is_collision(curr_rock_index, rock_x - 1, rock_y):
                        self.debugContext.print(4, f"rock collided on leftward jet")
                    #            collision = True
                    # break
                    else:
                        rock_x = rock_x - 1
                if self.is_collision(curr_rock_index, rock_x, rock_y - 1):
                    self.debugContext.print(4, f"rock collided on drop")
                    collision = True
                    break
                elif self.is_rest(curr_rock_index, rock_x, rock_y):
                    self.debugContext.print(4, f"rock came to rest")
                    collision = True
                    break
                else:
                    rock_drop_depth = rock_drop_depth + 1
                    rock_y = rock_y - 1
                self.jet_index = self.jet_index + 1
            self.jet_index = self.jet_index + 1
            self.debugContext.print(3, f"adding rock to map at {rock_x}, {rock_y}")
            self.add_rock_to_map(curr_rock_index, rock_x, rock_y)
            self.debugContext.print(3, f"printing map after rock")
            self.debugContext.print(3, "")
            if rock_y + rock_height > self.max_height:
                self.max_height_differential.append((rock_y + rock_height) - self.max_height)
                self.max_height = rock_y + rock_height
            else:
                self.max_height_differential.append(0)
            # self.max_height = self.max_height + rock_height
            self.debugContext.print(2,
                                    f"max height is now {self.max_height}, changed by {self.max_height_differential[-1]}")
            if rock_drop_depth > self.max_drop:
                self.max_drop = rock_drop_depth
            self.current_rock = self.current_rock + 1
            self.debugContext.decrease_indent()
        if self.current_rock < self.num_rocks:
            self.debugContext.print(2, f"Looks like we detected a cycle and dropped out of the loop early")
            self.debugContext.print(2, f"so need to calculate additional height")
            self.cycle_end = self.current_rock
            self.cycle_begin = matching_cycle_indexes[0]
            self.cycle_length = self.cycle_end - self.cycle_begin
            self.each_cycle_adds_height = sum(self.max_height_differential[self.cycle_begin: self.cycle_end + 1])
            self.debugContext.print(2, f"each cycle starts at {self.cycle_begin}, ends at {self.cycle_end},")
            self.debugContext.print(2, f"so is {self.cycle_length} long,")
            self.debugContext.print(2, f"and adds {self.each_cycle_adds_height} to the height")
            height_from_cycles = (((
                                               self.num_rocks - 1) - self.current_rock) // self.cycle_length) * self.each_cycle_adds_height
            num_leftover_rocks = (self.num_rocks - self.current_rock) % self.cycle_length
            self.debugContext.print(2, f"num leftover rocks is {num_leftover_rocks}")
            height_from_partial_cycle = sum(self.max_height_differential[self.cycle_begin: self.cycle_begin + (
                        (self.num_rocks - self.current_rock) % self.cycle_length)])
            self.debugContext.print(2,
                                    f"adding values from beginning of cycle to {self.cycle_begin + ((self.num_rocks - self.current_rock) % self.cycle_length)}")
            self.debugContext.print(2,
                                    f"current height {self.max_height} + cycles {height_from_cycles} + {height_from_partial_cycle} =")
            self.max_height = self.max_height + height_from_cycles + height_from_partial_cycle

        self.debugContext.decrease_indent()
        self.debugContext.print(3, f"max drop was {self.max_drop}")
        self.debugContext.print(1, f"Height is {self.max_height}")
        return self.max_height

    def get_rock_size(self, rock_index) -> tuple:
        if self.rocks[rock_index].ndim == 1:
            return len(self.rocks[rock_index]), 1
        else:
            return self.rocks[rock_index].shape[1], len(self.rocks[rock_index])

    def add_rock_to_map(self, rock, x, y):
        rock_width, rock_height = self.get_rock_size(rock)
        for test_y in range(0, rock_height):
            for test_x in range(0, rock_width):
                if self.rocks[rock].ndim == 1:
                    if self.rocks[rock][test_x] == 1:
                        self.map[y + test_y][x + test_x] = 1
                else:
                    if self.rocks[rock][test_y][test_x] == 1:
                        self.map[y + test_y][x + test_x] = 1

    def print_rock_on_map(self, rock, x, y):
        tmp_map = self.map.copy()
        rock_width, rock_height = self.get_rock_size(rock)
        for test_y in range(0, rock_height):
            for test_x in range(0, rock_width):
                if self.rocks[rock].ndim == 1:
                    if self.rocks[rock][test_x] == 1:
                        tmp_map[y + test_y][x + test_x] = 2
                else:
                    if self.rocks[rock][test_y][test_x] == 1:
                        tmp_map[y + test_y][x + test_x] = 2
        self.debugContext.print(5, "")
        for i in range(tmp_map.shape[0] - 1, -1, -1):
            # self.debugContext.print(5, tmp_map[i])
            self.debugContext.print(5, ['#' if x == 1 else '@' if x == 2 else '.' for x in tmp_map[i].tolist()])
        self.debugContext.print(5, "")

    # determines if there's a collision with the current pattern if rock x and rock y
    def is_collision(self, rock, x, y):
        rock_width, rock_height = self.get_rock_size(rock)
        self.debugContext.print(4,
                                f"checking for collision with height {rock_height}, width {rock_width}, and coordinates {x}, {y}")
        if y < 0:
            self.debugContext.print(4, f"rock collides because y < 0")
            return True
        elif x < 0:
            self.debugContext.print(4, f"rock collides because x < 0")
            return True
        elif x + rock_width - 1 > 6:
            self.debugContext.print(4, f"rock collides because x + rock is out of bounds")
            return True
        for test_y in range(0, rock_height):
            for test_x in range(0, rock_width):
                if self.rocks[rock].ndim == 1:
                    if self.rocks[rock][test_x] == 1:
                        if self.map[y + test_y][x + test_x] == 1:
                            return True
                elif self.rocks[rock][test_y][test_x] == 1:
                    if self.map[y + test_y][x + test_x] == 1:
                        return True
        return False

    def is_rest(self, rock, x, y):
        rock_width, rock_height = self.get_rock_size(rock)
        for test_y in range(0, rock_height):
            for test_x in range(0, rock_width):
                if self.rocks[rock].ndim == 1:
                    if self.rocks[rock][test_x] == 1:
                        if self.map[y + test_y - 1][x + test_x] == 1:
                            return True
                elif self.rocks[rock][test_y][test_x] == 1:
                    if self.map[y + test_y - 1][x + test_x] == 1:
                        return True
        return False

    def get_map(self):
        return self.map


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level, num_rocks=2022):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.my_map = DropMap(7, 8, debug_context=self.debug, num_rocks=num_rocks)

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        self.my_map.print()

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    self.my_map.add_jets(line)
                else:
                    pass

    def solve(self):
        self.print_run_info()
        self.parse()
        self.print()
        self.my_map.print_rocks()
        if self.puzzle_part == "a":
            return self.my_map.drop_rocks()
        else:
            return self.my_map.drop_rocks()

    def test_setup(self):
        self.my_map = DropMap(7, 8)
        self.print()
        self.my_map.add_rock_to_map(1, 0, 0)
        self.print()
        return self.my_map.get_map()
