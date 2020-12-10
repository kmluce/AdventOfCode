import fileinput

class TobogganMap:
    def __init__(self):
        self.map = []

    def read_map(self):
        for line in fileinput.input():
            self.map.append(line.rstrip())

    def print_map(self):
        print('\n'.join(self.map))

#TODO finish rest of problem

if __name__ == '__main__':
    toboggan = TobogganMap()

    toboggan.read_map()
    toboggan.print_map()