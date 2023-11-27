import fileinput
import copy

class ConwayHyperCube():
    def __init__(self):
        self.currCube = []
        self.priorCube = []
        self.origInput = []
        self.borderSize = 6
        self.currCubeWidth = 0
        self.currCubeHeight = 0
        self.currCubeDepth = 0
        self.currCubeHyp = 0
        self.priorCubeWidth = 0
        self.priorCubeHeight = 0
        self.priorCubeDepth = 0
        self.priorCubeHyp = 0


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
        self.currCubeHyp = 1

    def initialize_cube(self):
        # note:  list comprehensions need to run backwards of how you use them to make the correct dimension
        #        so, for instance, you use hyper dimension first, but it needs to be instantiated last
        self.currCube = [[[['.' for col in range(self.currCubeWidth)] \
                           for col in range(self.currCubeHeight)] \
                         for col in range(self.currCubeDepth)]  \
                         for col in range(self.currCubeHyp)]
        self.print_cube()
        for y, line in enumerate(self.origInput):
            for x, char in enumerate(line):
                #print(" setting w=0, z=0, x=", x, "y=", y, "to", char)
                self.currCube[0][0][y][x] = char
        self.print_cube()

    def print_total_active(self):
        totalActive = 0
        for w, hyp in enumerate(self.currCube):
            for z, face in enumerate(hyp):
                for y, row in enumerate(face):
                    for x, col in enumerate(row):
            #            print("checking value at", z, y, x)
                        if self.currCube[w][z][y][x] == '#':
                            totalActive +=1
        print("NOTE: cube contains", totalActive, "active cubes")

    def rotate_cube(self):
        self.priorCube = copy.deepcopy(self.currCube)
        self.priorCubeHeight = self.currCubeHeight
        self.priorCubeWidth = self.currCubeWidth
        self.priorCubeDepth = self.currCubeDepth
        self.priorCubeHyp = self.currCubeHyp

        # then increment the current ones
        self.currCubeWidth += 2
        self.currCubeHeight += 2
        self.currCubeDepth += 2
        self.currCubeHyp += 2
        self.currCube = [[[['.' for col in range(self.currCubeWidth)] \
                           for col in range(self.currCubeHeight)] \
                          for col in range(self.currCubeDepth)] \
                         for col in range(self.currCubeHyp)]
        self.print_cube()

    def check_cube_neighbors(self, w, z, y, x):
        totalActiveNeighbors = 0
        #print("checking cube for", z, y , x)
        for checkW in range(w-1, w+2):
            for checkZ in range(z-1, z+2):
                for checkY in range(y-1, y+2):
                    for checkX in range(x-1, x+2):
                        #print ("    checking neighbor", checkZ, checkY, checkX)
                        checkPW = checkW -1
                        checkPZ = checkZ -1
                        checkPY = checkY -1
                        checkPX = checkX -1
                        #print ("      prior neighbor is", checkPZ, checkPY, checkPX)
                        if self.is_valid_prior_addy(checkPW, checkPZ,checkPY,checkPX):
                            if checkW == w and checkX == x and checkY == y and checkZ == z:
                                next
                            else:
                                if self.priorCube[checkPW][checkPZ][checkPY][checkPX] == '#':
                            #        print("      found active neighbor")
                                    totalActiveNeighbors += 1
                        else:
                            pass
                            #print("      ", checkPZ, checkPX, checkPY, "is not a valid address in PriorCube")
        return totalActiveNeighbors

    def is_valid_prior_addy(self, w, z, y, x):
        validPriorAddy = True
        if w < 0 or w >= self.priorCubeHyp:
            validPriorAddy = False
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
        for w in range(self.currCubeHyp):
            myNeighbors = 0
            for z in range(self.currCubeDepth):
                for y in range(self.currCubeHeight):
                    for x in range(self.currCubeWidth):
                        #print("  checking neighbors for", w, z, y, x, "whose value is", self.priorCube[w][z][y][x])
                        print("  checking neighbors for", w, z, y, x)
                        myNeighbors = self.check_cube_neighbors(w,z,y,x)
                        print("    ", myNeighbors, "active neighbors.")
                        if self.is_valid_prior_addy(w-1,z-1,y-1,x-1):
                            if self.priorCube[w-1][z-1][y-1][x-1] == '#':
                                if myNeighbors == 2 or myNeighbors == 3:
                                    self.currCube[w][z][y][x] = '#'
                            elif self.priorCube[w-1][z-1][y-1][x-1] == '.':
                                if myNeighbors == 3:
                                    self.currCube[w][z][y][x] = '#'
                        else:
                            if myNeighbors == 3:
                                self.currCube[w][z][y][x] = '#'

    def print_cube(self):
        print()
        print("Cube is", self.currCubeWidth, "wide,", self.currCubeHeight, "tall, and", self.currCubeDepth, "deep:")
        for w, hyp in enumerate(self.currCube):
            for z, line in enumerate(hyp):
                print ("z=", z, "w=", w)
                for x, row in enumerate(line):
                    print("  ", line[x])
                print()
        self.print_total_active()


if __name__ == '__main__':
    myCube = ConwayHyperCube()
    myCube.input_cube()
    myCube.print_cube()
    myCube.initialize_cube()

#    myCube.rotate_cube()
#    myCube.do_generation()
#    myCube.print_cube()
    for i in range(6):
        print("generation:", i+1)
        myCube.rotate_cube()
        myCube.do_generation()
        myCube.print_cube()
