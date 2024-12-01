from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.left_loc = []
        self.right_loc = []
        self.sortedRightLoc = []
        self.sortedLeftLoc = []
        self.distances = 0
        self.similarities = 0

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip().split()
                    self.left_loc.append(int(line[0]))
                    self.right_loc.append(int(line[1]))
                else:
                    pass
        self.sortedRightLoc = sorted(self.right_loc)
        self.sortedLeftLoc = sorted(self.left_loc)
        for i in range(0, len(self.sortedRightLoc)):
            self.distances += abs(self.sortedRightLoc[i] - self.sortedLeftLoc[i])

    def similarity(self):
        for i in range(0, len(self.sortedRightLoc)):
            self.similarities += (self.sortedLeftLoc[i] * self.sortedRightLoc.count(self.sortedLeftLoc[i]))

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.distances
        else:
            self.similarity()
            return self.similarities
