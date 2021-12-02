
class Puzzle:
    def __init__(self, fileName):
        self.fileName= fileName

    def parse(self):
        with open(self.fileName) as file:
           for line in file:
                line = line.rstrip()

    def solvea(self):
        return None