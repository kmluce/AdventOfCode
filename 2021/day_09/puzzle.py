class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.tubeMap = []
        self.riskLevelSum = 0
        self.lowest_points = []
        self.visited = []
        self.tmp_basin_size = 0
        self.basin_sizes = []

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                self.tubeMap.append([int(i) for i in line])

    def find_risk(self, x, y):
        found_lower = 0
        for test_y in range(-1, 2):
            curr_y = y + test_y
            if (curr_y < 0) or (curr_y > len(self.tubeMap) - 1):
                continue
            for test_x in range(-1, 2):
                curr_x = x + test_x
                if (curr_x < 0) or (curr_x > len(self.tubeMap[y]) - 1):
                    continue
                elif abs(test_x) == abs(test_y):
                    continue
                else:
                    # print("  checking", curr_x, ",", curr_y)
                    # print("       and it is", self.tubeMap[curr_y][curr_x])
                    if self.tubeMap[curr_y][curr_x] <= self.tubeMap[y][x]:
                        found_lower = found_lower + 1
                    if found_lower > 0:
                        break
            if found_lower > 0:
                break
        if found_lower == 0:
            self.lowest_points.append([x, y])
            return self.tubeMap[y][x] + 1
        else:
            return 0

    def find_basin_size(self, point):
        x = point[0]
        y = point[1]
        self.tmp_basin_size = 0
        self.visited = [point]
        self.get_basin_recursively(x, y)
        self.basin_sizes.append(self.tmp_basin_size)

    def get_basin_recursively(self, x, y):
        for test_y in range(-1, 2):
            curr_y = y + test_y
            if (curr_y < 0) or (curr_y > len(self.tubeMap) - 1):
                continue
            for test_x in range(-1, 2):
                curr_x = x + test_x
                if (curr_x < 0) or (curr_x > len(self.tubeMap[y]) - 1):
                    continue
                elif abs(test_x) == abs(test_y):
                    continue
                elif [curr_x, curr_y] in self.visited:
                    continue
                else:
                    # print("  checking", curr_x, ",", curr_y)
                    # print("       and it is", self.tubeMap[curr_y][curr_x])
                    self.visited.append([curr_x, curr_y])
                    if self.tubeMap[curr_y][curr_x] < 9:
                        self.tmp_basin_size += 1
                        self.get_basin_recursively(curr_x, curr_y)
        return

    def solve_a(self):
        total_risk = 0
        # print("Initial map is")
        for line in self.tubeMap:
            print("  ", line)
        for y, line in enumerate(self.tubeMap):
            for x, height in enumerate(line):
                # print("evaluating", x, y, "which is", self.tubeMap[y][x])
                total_risk = total_risk + self.find_risk(x, y)
        return total_risk

    def solve_b(self):
        for line in self.tubeMap:
            print("  ", line)
        for y, line in enumerate(self.tubeMap):
            for x, height in enumerate(line):
                # print("evaluating", x, y, "which is", self.tubeMap[y][x])
                self.find_risk(x, y)
        for point in self.lowest_points:
            print("finding basin for point", point)
            self.find_basin_size(point)
        print(self.basin_sizes.sort())
