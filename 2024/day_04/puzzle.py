from utils.debugging import PrintDebug
import re


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
        self.xmas_re = re.compile("XMAS")
        self.total_xmas = 0


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

    # I made a lot of amusing work for myself by wanting to handle this with list comprehensions
    # It required me to learn to rotate a matrix so that the diagonals were rows
    # This is a skill that's probably not necessary for many real-life problems
    def splice_lists(self):
        tmp_list = [[m[i] for m in self.search_field] for i in range(len(self.search_field[0]))]
        self.vertical_search_field = [''.join(a) for a in tmp_list]
        print("original search field:")
        self.print_array(self.search_field)
        print()
        print("vertical search field:")
        self.print_array(self.vertical_search_field)
        print()
        print("vertical search field:")
        self.right_diagonal = self.make_right_diagonal(self.search_field)
        self.print_array(self.right_diagonal)
        print()
        print("vertical search field:")
        self.left_diagonal = self.make_left_diagonal(self.search_field)
        self.print_array(self.left_diagonal)
        print()

    def make_left_diagonal(self, matrix):
        new_matrix = []
        height = len(matrix)
        width = len(matrix[0])
        for k in range(width + height - 1):
            new_matrix.append('')
            for j in range(k + 1):
                i = k - j
                if j < height and i < width:
                    self.debug.print(3, f"appending {matrix[j][i]} to new_matrix[{k}]")
                    new_matrix[k] += matrix[j][i]
        return new_matrix

    def make_right_diagonal(self, matrix):
        new_matrix = []
        height = len(matrix)
        width = len(matrix[0])
        for k in range(width + height - 1):
            new_matrix.append('')
            for j in range(k + 1):
                i = k - j
                if j < height and i < width:
                    self.debug.print(3, f"appending {matrix[j][width - i - 1]} to new_matrix[{k}]")
                    new_matrix[k] += matrix[j][width-i-1]
        return new_matrix

    def test_splices(self):
        test = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]
        print("original test:")
        self.print_array(test)
        print()
        print("vertical test:")
        tmp_list = [[m[i] for m in test] for i in range(len(test[0]))]
        self.print_array(tmp_list)
        print()
        print("original test:")
        self.print_array(test)
        print()
        print("left diagonal test:")
        self.print_array(self.make_left_diagonal(test))
        print()
        print("right diagonal test:")
        self.print_array(self.make_right_diagonal(test))

    @staticmethod
    def print_array(array):
        print(array)
        for i in range(len(array)):
            for j in range(len(array[i])):
                print(array[i][j], end=" ")
            print()

    def find_all_words(self):
        instances_of_xmas = [ len(self.xmas_re.findall(line)) for line in self.search_field]
        print("searching for horizontal words in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)
        instances_of_xmas = [ len(self.xmas_re.findall(line[::-1])) for line in self.search_field]
        print("searching for horizontal words backwards in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)

        instances_of_xmas = [ len(self.xmas_re.findall(line)) for line in self.vertical_search_field]
        print("searching for vertical words in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)
        instances_of_xmas = [ len(self.xmas_re.findall(line[::-1])) for line in self.vertical_search_field]
        print("searching for vertical words backwards in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)

        instances_of_xmas = [ len(self.xmas_re.findall(line)) for line in self.right_diagonal]
        print("searching for right diagonal words in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)
        instances_of_xmas = [ len(self.xmas_re.findall(line[::-1])) for line in self.right_diagonal]
        print("searching for right diagonal words backwards in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)

        instances_of_xmas = [ len(self.xmas_re.findall(line)) for line in self.left_diagonal]
        print("searching for left diagonal words in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)
        instances_of_xmas = [ len(self.xmas_re.findall(line[::-1])) for line in self.left_diagonal]
        print("searching for left diagonal words backwards in search field:", instances_of_xmas)
        self.total_xmas += sum(instances_of_xmas)

        print("total instances of XMAS:", self.total_xmas)

        return self.total_xmas

    def solve_part_b(self):
        for row in range(1, len(self.search_field) - 1):
            index_tmp = [ i for i, ltr in enumerate(self.search_field[row]) if ltr == "A"]
            # need to exclude the first and last columns
            indices_of_a = [index for index in index_tmp if 0 < index < len(self.search_field[row]) - 1]
            for index in indices_of_a:
                if ((self.search_field[row-1][index-1] == "M" and self.search_field[row+1][index+1] == "S")
                    or (self.search_field[row - 1][index - 1] == "S" and self.search_field[row + 1][index + 1] == "M")):
                    if ((self.search_field[row - 1][index + 1] == "M" and self.search_field[row + 1][index - 1] == "S")
                        or (self.search_field[row - 1][index + 1] == "S"
                            and self.search_field[row + 1][index - 1] == "M")):
                                self.total_xmas += 1


    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            self.splice_lists()
            return self.find_all_words()
        else:
            self.solve_part_b()
            return self.total_xmas
