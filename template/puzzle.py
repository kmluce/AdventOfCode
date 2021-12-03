class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()

    def solvea(self):
        return None
