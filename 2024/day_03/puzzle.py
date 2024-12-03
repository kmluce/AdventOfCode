from utils.debugging import PrintDebug
import re


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self._sum_of_products = 0
        self._data = []

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
                    self._data.append(line)
                    print("line is", line)
                    if self.puzzle_part == 'b':
                        while True:
                            new_line = re.sub(r"don't\(\).*?do\(\)", "", line)
                            if new_line == line:
                                break
                            line = new_line
                        # Catch the case where the don't() doesn't have a matching do()
                        new_line = re.sub(r"don't\(\).*", "", line)
                        line = new_line
                        print()
                        print("line b is :", line)
                    # p = re.compile(r"mul\((\d+),(\d+)\)")
                    p = re.compile(r"mul\((\d+),(\d+)\)")
                    print(p.search(line).span())
                    matches = p.search(line)
                    if matches:
                        print("matching group is", matches.group())
                    else:
                        print("no match found")
                    matches2 = p.findall(line)
                    if matches2:
                        for match in matches2:
                            print(match)
                            self._sum_of_products += int(match[0]) * int(match[1])
                else:
                    pass

    def process_errors_part_b(self):
        self._sum_of_products = 0
        bigline=""
        for line in self._data:
            bigline += line
        while True:
            new_line = re.sub(r"don't\(\).*?do\(\)", "", bigline)
            if new_line == bigline:
                break
            bigline = new_line
        # Catch the case where the don't() doesn't have a matching do()
        new_line = re.sub(r"don't\(\).*", "", bigline)
        bigline = new_line
        print()
        print("line b is :", bigline)
        p = re.compile(r"mul\((\d+),(\d+)\)")
        print(p.search(bigline).span())
        matches = p.search(bigline)
        if matches:
            print("matching group is", matches.group())
        else:
            print("no match found")
        matches2 = p.findall(bigline)
        if matches2:
            for match in matches2:
                print(match)
                self._sum_of_products += int(match[0]) * int(match[1])

    def solve(self):
        self.print_run_info()
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self._sum_of_products
        else:
            self.process_errors_part_b()
            return self._sum_of_products
