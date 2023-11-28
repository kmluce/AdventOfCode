from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def get_cube_faces(self, x, y, z):
        point_list = [[_a, _b, _c] for _a in [x, x + 1] for _b in [y, y + 1] for _c in [z, z + 1]]
        tmp_face_list = [[_a for _a in point_list if _a[_b] == _c] for _b in [0, 1, 2] for _c in
                         [x, x + 1, y, y + 1, z, z + 1]]
        face_list = [_x for _x in tmp_face_list if _x != []]
        return face_list

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.all_faces =[]

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
                    print(self.get_cube_faces(*[int(_x) for _x in line.split(',')]))
                    self.all_faces.extend(self.get_cube_faces(*[int(_x) for _x in line.split(',')]))
                else:
                    pass


    def get_count_of_unshared_faces(self):
        print(self.all_faces)

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            self.get_count_of_unshared_faces()
            return 0
        else:
            return 0
