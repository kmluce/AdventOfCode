import fileinput

class TobogganMap:
    def __init__(self):
        self.map = []

    def read_map(self):
        for line in fileinput.input():
            self.map.append(line.rstrip())

    def print_map(self):
        print('\n'.join(self.map))

    def check_map(self, step_x, step_y):
        x = 0
        total_trees=0
        for y in range(len(self.map), step_y):
            if self.map[y][x] == '#':
                print(" tree at ", y, ",", x)
                total_trees += 1
            





#TODO finish rest of problem

if __name__ == '__main__':
    toboggan = TobogganMap()

    toboggan.read_map()
    toboggan.print_map()