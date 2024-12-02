from utils.debugging import PrintDebug
import copy


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.levelData = []
        self.distances = []
        self.safe = 0
        self.unsafeData = []

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
                    level = [int(x) for x in line]
                    distance = [level[y] - level[y-1] for y in range(1, len(level))]
                    print(f"level is {level} ; distance is {distance}")
                    self.levelData.append(level)
                    self.distances.append(distance)
                    if (len([x for x in distance if x > 0]) == len(distance)) \
                            or (len([x for x in distance if x < 0]) == len(distance)):
                        print("    all increasing or decreasing")
                        if len([x for x in distance if (x > 3 or x < -3)]) == 0:
                            print("        all increasing gently")
                            self.safe += 1
                        else:
                            self.unsafeData.append(level)
                    else:
                        self.unsafeData.append(level)
                else:
                    pass

    def reprocess_data(self):
        for newLevel in self.unsafeData:
            print("reprocess level is", newLevel)
            for x, item in enumerate(newLevel):
                myLevel = copy.deepcopy(newLevel)
                myLevel.pop(x)
                if self.check_safety(myLevel):
                    self.safe += 1
                    break

    def check_safety(self, levelData):
        print("    checking safety of ", levelData)
        distance = [levelData[y] - levelData[y - 1] for y in range(1, len(levelData))]
        if (len([x for x in distance if x > 0]) == len(distance)) or \
                (len([x for x in distance if x < 0]) == len(distance)):
            print("    all increasing or decreasing")
            if len([x for x in distance if (x > 3 or x < -3)]) == 0:
                print("        all increasing gently")
                return True
            else:
                return False

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            print("unsafe levels are", len(self.unsafeData))
            return self.safe
        else:
            print("unsafe data is", self.unsafeData)
            print("unsafe levels are", len(self.unsafeData))
            self.reprocess_data()
            return self.safe
