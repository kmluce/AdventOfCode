class Forest:
    def __init__(self):
        self.treemap = []
        self.l_visible = []  # trees visible from left
        self.scenic = []

    def add_line(self, line):
        self.treemap.append([int(x) for x in line])
        # self.print()

    def print(self):
        print("treemap:")
        for line in self.treemap:
            print("  ", line)
        print("l_visible:")
        for line in self.l_visible:
            print("  ", line)
        print("scenic:")
        for line in self.scenic:
            print("  ", line)

    def find_scenic(self):
        print("entering find_scenic")
        self.scenic = [[0 for _ in group] for group in self.treemap]
        self.print()
        for tree_y in range(1, len(self.treemap) - 1):
            for treex in range(1, len(self.treemap[0]) - 1):
                d_trees = 0
                u_trees = 0
                r_trees = 0
                l_trees = 0
                for curr_y in range(tree_y + 1, len(self.treemap)):
                    d_trees += 1
                    if self.treemap[curr_y][treex] >= self.treemap[tree_y][treex]:
                        break
                for curr_y in range(tree_y - 1, -1, -1):
                    u_trees += 1
                    if self.treemap[curr_y][treex] >= self.treemap[tree_y][treex]:
                        break
                for curr_x in range(treex + 1, len(self.treemap[0])):
                    r_trees += 1
                    if self.treemap[tree_y][curr_x] >= self.treemap[tree_y][treex]:
                        break
                for curr_x in range(treex - 1, -1, -1):
                    l_trees += 1
                    if self.treemap[tree_y][curr_x] >= self.treemap[tree_y][treex]:
                        break
                self.scenic[tree_y][treex] = d_trees * u_trees * l_trees * r_trees

    def process_maps(self):
        self.l_visible = [[0 for _ in group] for group in self.treemap]
        #    self.scenic = self.l_visible
        self.print()
        # calculate left-wise
        for j in range(0, len(self.treemap)):
            highest_left = self.treemap[j][0]
            self.l_visible[j][0] = 1
            for i in range(1, len(self.treemap[j])):
                if self.treemap[j][i] > highest_left:
                    self.l_visible[j][i] = 1 | self.l_visible[j][i]
                    highest_left = self.treemap[j][i]
        # calculate right-wise:
        for j in range(0, len(self.treemap)):
            highest_right = self.treemap[j][-1]
            self.l_visible[j][-1] = 1
            for i in reversed(range(1, len(self.treemap[j]))):
                if self.treemap[j][i] > highest_right:
                    self.l_visible[j][i] = 1 | self.l_visible[j][i]
                    highest_right = self.treemap[j][i]
        # calculate from above:
        for i in range(0, len(self.treemap[0])):  # counting on the map being rectangular, here
            highest_above = self.treemap[0][i]
            self.l_visible[0][i] = 1
            for j in range(1, len(self.treemap)):
                if self.treemap[j][i] > highest_above:
                    self.l_visible[j][i] = 1 | self.l_visible[j][i]
                    highest_above = self.treemap[j][i]
        # calculate from below:
        for i in range(0, len(self.treemap[0])):  # counting on the map being rectangular, here
            highest_below = self.treemap[-1][i]
            self.l_visible[-1][i] = 1
            for j in reversed(range(1, len(self.treemap))):
                if self.treemap[j][i] > highest_below:
                    self.l_visible[j][i] = 1 | self.l_visible[j][i]
                    highest_below = self.treemap[j][i]
        self.print()

    def visible_trees(self):
        tree_total = 0
        for i in self.l_visible:
            tree_total = tree_total + sum(i)
        return tree_total

    def most_scenic(self):
        self.print()
        return max(max(x) for x in self.scenic)


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part):
        self.forest = Forest()
        self.fileName = file_name
        self.puzzle_part = puzzle_part

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    self.forest.add_line(line.rstrip())
                else:
                    pass
            self.forest.process_maps()
            self.forest.find_scenic()

    def print(self):
        pass

    def solve(self):
        self.print()
        if self.puzzle_part == "a":
            return self.forest.visible_trees()
        else:
            return self.forest.most_scenic()
