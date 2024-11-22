from utils.debugging import PrintDebug

class OasisDiagnostics:
    def __init__(self, oasis_output, puzzle_part):
        self.oasis_output = oasis_output
        self.readout = [ [ int(i) for i in oasis_output.split(" ")]]
        self.puzzle_part = puzzle_part
        # self.print_oasis()
        self.hydrate()

    def hydrate(self):
        while len(set(self.readout[-1])) != 1:
            self.readout.append([self.readout[-1][i] - self.readout[-1][i-1] for i in range(1, len(self.readout[-1]))])
        self.readout.append([0] * (len(self.readout[-1]) -1 ))
        # self.print_oasis()
        if self.puzzle_part == 'a':
            self.extrapolate_forwards()
        else:
            self.extrapolate_backwards()
        self.print_oasis()

    def extrapolate_backwards(self):
        for i in range(len(self.readout)-2, -1, -1):
            # print(i)
            self.readout[i].insert(0, self.readout[i][0] - self.readout[i+1][0])

    def extrapolate_forwards(self):
        # print(f"counting rows from {len(self.readout)-2} to 0")
        for i in range(len(self.readout)-2, -1, -1):
            # print(i)
            self.readout[i].append(self.readout[i][-1] + self.readout[i+1][-1])

    def print_oasis(self):
        print(f"{self.readout}")

    def get_extrapolated_rvalue(self):
        return self.readout[0][-1]

    def get_extrapolated_lvalue(self):
        return self.readout[0][0]


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.oasis_diagnostics = []

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print_puzzle(self):
        print("Diagnostics:")
        for i in range(0, len(self.oasis_diagnostics)):
            print(f"{i}: ", end="")
            self.oasis_diagnostics[i].print_oasis()
        print()

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    self.oasis_diagnostics.append(OasisDiagnostics(line, self.puzzle_part))
                    # self.print_puzzle()
                else:
                    pass


    def solve(self):
        self.print_run_info()
        self.parse()
        # self.print_puzzle()
        if self.puzzle_part == "a":
            return sum([ i.get_extrapolated_rvalue() for i in self.oasis_diagnostics ])
        else:
            return sum([ i.get_extrapolated_lvalue() for i in self.oasis_diagnostics ])
