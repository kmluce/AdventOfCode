class Puzzle():
    def __init__(self, fileName):
        self.fileName= fileName
        self.depth = 0
        self.horizontalPos =0
        self.aim = 0

    def parsea(self):
        with open(self.fileName) as file:
           for line in file:
                line = line.rstrip()
                fields =line.split()
                #print("field 1", fields[0], "field 2", fields[1])
                if fields[0] == "forward":
                   self.horizontalPos += int(fields[1])
                elif fields[0] == "down":
                    self.depth += int(fields[1])
                elif fields[0] == "up":
                    self.depth -= int(fields[1])
                else:
                    print("Error!  line", line, "not parsed correctly")
        return None

    def parseb(self):
        with open(self.fileName) as file:
           for line in file:
                line = line.rstrip()
                fields =line.split()
                #print("field 1", fields[0], "field 2", fields[1])
                if fields[0] == "forward":
                   self.horizontalPos += int(fields[1])
                   self.depth += int(fields[1]) * self.aim
                elif fields[0] == "down":
                    self.aim += int(fields[1])
                elif fields[0] == "up":
                    self.aim -= int(fields[1])
                else:
                    print("Error!  line", line, "not parsed correctly")
        return None

    def solvea(self):
        return self.depth * self.horizontalPos