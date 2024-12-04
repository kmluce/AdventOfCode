from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.search_field = []
        self.vertical_search_field = []
        self.left_diagonal = []
        self.right_diagonal = []


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
                    self.search_field.append(line)
                else:
                    pass

    def splice_lists(self):
        tmp_list = [[m[i] for m in self.search_field] for i in range(len(self.search_field[0]))]
        self.vertical_search_field = [''.join(a) for a in tmp_list]
        print("original search field:")
        print(self.search_field)
        print()
        print("rotated search field:")
        print(self.vertical_search_field)

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            self.splice_lists()
            return 0
        else:
            return 0
