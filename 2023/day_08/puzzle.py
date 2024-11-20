import math
from typing import Any
from utils.debugging import PrintDebug

class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.map = {}
        self.directions = ''
        self.end_state = 'ZZZ'
        self.beginning_node = 'AAA'

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")
    def print(self):
        pass

    def run_map(self):
        curr_step = 0
        curr_node = self.beginning_node
        # print("directions is ", self.directions)
        while curr_node != self.end_state:
            curr_step += 1
            direction = self.directions[(curr_step % len(self.directions)) -1]
            if direction == 'R':
                dir_num = 1
            else:
                dir_num = 0
            # print("curr direction is ", direction)
            new_node = self.map[curr_node][dir_num]
            # print("new node is ", new_node, flush=True)
            curr_node = new_node
        return curr_step

    def shortest_path_to_z(self, node):
        current_node = node
        current_step = 0

        while current_node[2] != 'Z':
            current_step += 1
            direction = self.directions[(current_step % len(self.directions)) - 1]
            if direction == 'R':
                next_node = self.map[current_node][1]
            else:
                next_node = self.map[current_node][0]
            current_node = next_node
        return current_step



    def ghost_map(self):
        current_nodes: list[Any] = [ i for i in self.map.keys() if i[2] == 'A' ]
        answers = [ int(self.shortest_path_to_z(i)) for i in current_nodes ]
        return math.lcm(*answers)

    def parallel_run_map(self):
        current_nodes = [ i for i in self.map.keys() if i[2] == 'A' ]
        end_nodes = ['Z'] * len(current_nodes)
        print(f"Starting Nodes: {current_nodes}")
        print(f"End Nodes: {end_nodes}")
        curr_step = 0

        while [ i[2] for i in current_nodes ] != end_nodes:
            curr_step += 1
            direction = self.directions[(curr_step % len(self.directions)) - 1]
            if direction == 'R':
                next_nodes = [ self.map[i][1] for i in current_nodes ]
            else:
                next_nodes = [ self.map[i][0] for i in current_nodes ]
            print(f"step {curr_step} nodes are {next_nodes}", flush=True)
            current_nodes = next_nodes
            # print(flush=True)
        return curr_step

    def parse(self):
        with open(self.fileName) as file:
            self.directions = file.readline().strip()
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    # print(line)
                    line = line.replace(" = (", ",")
                    line = line.replace(", ", ",")
                    line = line.replace(")", "")
                    # print(line, flush=True)
                    first_parse = line.split(",")
                    self.map[first_parse[0]] = [first_parse[1], first_parse[2]]
                else:
                    pass

    def solve(self):
        print()
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.run_map()
        else:
            return self.ghost_map()
