import fileinput
import copy

class ConwayCube():
    def __init__(self):
        self.currCube = []
        self.priorCube = []
        self.origInput = []
        self.borderSize = 6
        self.currCubeWidth = 0
        self.currCubeHeight = 0
        self.currCubeDepth = 0
        self.priorCubeWidth = 0
        self.priorCubeHeight = 0
        self.priorCubeDepth = 0


    # reads in the original input
    # read in separately from initializing currCube so we can set size
    def input_cube(self):
        lineCount = 0
        for line in fileinput.input():
            line = line.rstrip()
            if fileinput.isfirstline():
                print("line is the first line and is", len(line), "characters wide")
            self.currCubeWidth = len(line)
            print("   line:", line)
            self.origInput.append(line)
            lineCount += 1
        self.currCubeHeight = lineCount
        self.currCubeDepth = 1

    def initialize_cube(self):
        self.currCube = [[['.' for col in range(self.currCubeWidth)] \
                          for col in range(self.currCubeHeight)] for col in range(self.currCubeDepth)]
        self.print_cube()
        for y, line in enumerate(self.origInput):
            for x, char in enumerate(line):
                print(" setting z=0, x=", x, "y=", y, "to", char)
                self.currCube[0][y][x] = char
        self.print_cube()

    def print_total_active(self):
        totalActive = 0
        for z, face in enumerate(self.currCube):
            for y, row in enumerate(face):
                for x, col in enumerate(row):
        #            print("checking value at", z, y, x)
                    if self.currCube[z][y][x] == '#':
                        totalActive +=1
        print("NOTE: cube contains", totalActive, "active cubes")

    def rotate_cube(self):
        self.priorCube = copy.deepcopy(self.currCube)
        self.priorCubeHeight = self.currCubeHeight
        self.priorCubeWidth = self.currCubeWidth
        self.priorCubeDepth = self.currCubeDepth
        # then increment the current ones
        self.currCubeWidth += 2
        self.currCubeHeight += 2
        self.currCubeDepth += 2
        #self.currCube = [[['.' for col in range(len(self.currCube[0][0])+1)] \
        #                  for col in range(len(self.currCube[0])+1)] \
        #                 for col in range(len(self.currCube)+1)]
        self.currCube = [[['.' for col in range(self.currCubeWidth)] \
                          for col in range(self.currCubeHeight)] for col in range(self.currCubeDepth)]
        self.print_cube()

    def check_cube_neighbors(self, z, y, x):
        totalActiveNeighbors = 0
        #print("checking cube for", z, y , x)
        for checkZ in range(z-1, z+2):
            for checkY in range(y-1, y+2):
                for checkX in range(x-1, x+2):
                    #print ("    checking neighbor", checkZ, checkY, checkX)
                    checkPZ = checkZ -1
                    checkPY = checkY -1
                    checkPX = checkX -1
                    #print ("      prior neighbor is", checkPZ, checkPY, checkPX)
                    if self.is_valid_prior_addy(checkPZ,checkPY,checkPX):
                        if checkX == x and checkY == y and checkZ == z:
                            next
                        else:
                            if self.priorCube[checkPZ][checkPY][checkPX] == '#':
                        #        print("      found active neighbor")
                                totalActiveNeighbors += 1
                    else:
                        pass
                        #print("      ", checkPZ, checkPX, checkPY, "is not a valid address in PriorCube")
        return totalActiveNeighbors

    def is_valid_prior_addy(self, z, y, x):
        validPriorAddy = True
        if z < 0 or z >= self.priorCubeDepth:
            validPriorAddy = False
        if y < 0 or y >= self.priorCubeHeight:
            validPriorAddy = False
        if x < 0 or x >= self.priorCubeWidth:
            validPriorAddy = False
        return validPriorAddy




    def do_generation(self):
        shiftSize = 1  # amount to shift old cube into new
        print("prior cube size is:", self.priorCubeDepth, self.priorCubeHeight, self.priorCubeWidth)
        for z in range(self.currCubeDepth):
            myNeighbors = 0
            for y in range(self.currCubeHeight):
                for x in range(self.currCubeWidth):
                    #print("  checking neighbors for", z, y, x, "whose value is", self.priorCube[z][y][x])
                    #print("  checking neighbors for", z, y, x)
                    myNeighbors = self.check_cube_neighbors(z,y,x)
                    #print("    ", myNeighbors, "active neighbors.")
                    if self.is_valid_prior_addy(z-1,y-1,x-1):
                        if self.priorCube[z-1][y-1][x-1] == '#':
                            if myNeighbors == 2 or myNeighbors == 3:
                                self.currCube[z][y][x] = '#'
                        elif self.priorCube[z-1][y-1][x-1] == '.':
                            if myNeighbors == 3:
                                self.currCube[z][y][x] = '#'
                    else:
                        if myNeighbors == 3:
                            self.currCube[z][y][x] = '#'

    def print_cube(self):
        print()
        print("Cube is", self.currCubeWidth, "wide,", self.currCubeHeight, "tall, and", self.currCubeDepth, "deep:")
        for z, line in enumerate(self.currCube):
            print ("z=", z)
            for x, row in enumerate(line):
                print("  ", line[x])
            print()
        self.print_total_active()


if __name__ == '__main__':
    myCube = ConwayCube()
    myCube.input_cube()
    myCube.print_cube()
    myCube.initialize_cube()
    for i in range(6):
        print("generation:", i+1)
        myCube.rotate_cube()
        myCube.do_generation()
        myCube.print_cube()
