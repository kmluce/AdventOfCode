from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.all_faces = []
        self.unshared_faces = []

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
                    for face in self.get_cube_faces(*[int(_x) for _x in line.split(',')]):
                        print(face)
                        # for row in face:
                        #     print(row)
                    # print(self.get_cube_faces(*[int(_x) for _x in line.split(',')]))
                    self.all_faces.extend(self.get_cube_faces(*[int(_x) for _x in line.split(',')]))
                else:
                    pass

    @staticmethod
    def get_cube_faces(x, y, z):
        face_list = []
        point_set = {(_a, _b, _c) for _a in (x, x + 1) for _b in (y, y + 1) for _c in (z, z + 1)}
        print("Point set is", point_set)
        tmp_face_list = [{_a for _a in point_set if _a[_b] == _c} for _b in (0, 1, 2) for _c in
                         (x, x + 1, y, y + 1, z, z + 1)]
        [face_list.append(_x) for _x in tmp_face_list if len(_x) != 0 and _x not in face_list]
        return face_list

    def get_count_of_unshared_faces(self):
        print("Number of faces is:", len(self.all_faces))
        print(self.all_faces)
        self.unshared_faces = [_x for _x in self.all_faces if self.all_faces.count(_x) == 1]
        print("Number of unshared faces is:", len(self.unshared_faces))
        return len(self.unshared_faces)

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.get_count_of_unshared_faces()
        else:
            return 0
