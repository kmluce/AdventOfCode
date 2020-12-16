import fileinput

class DockingData():
    def __init__(self):
        self.onesMask = 0
        self.zerosMaskComplement = 0
        self.zerosMask = 0
        self.memoryLocations = {}
        self.maskAnd = 68719476735   #2^36 -1 -- it's how you make bitwise complemented numbers not negative
        self.currentMask = 0
        self.memLocList = []

    def processInput(self):
        for line in fileinput.input():
            line = line.rstrip()
            print("line:", line)
            if 'mask' in line:
                self.onesMask = 0
                self.zerosMaskComplement = 0
                self.zerosMask = 0
                print("  line contains mask")
                maskParts = line.split()
                self.currentMask = maskParts[2]
                stringCount = 1
                for c in reversed(self.currentMask):
                    if c == '0':
                        print("    character is 0, so adding", stringCount, "to zeros mask complement.")
                        self.zerosMaskComplement += stringCount
                    elif c == '1':
                        print("    character is 1, so adding", stringCount, "to ones mask.")
                        self.onesMask += stringCount
                    stringCount *= 2
                self.zerosMask = ~ self.zerosMaskComplement & self.maskAnd
                print("  Ones mask is:", self.onesMask)
                print("  zeros mask complement is:", self.zerosMaskComplement)
                print("  zeros mask is:", self.zerosMask)
                print("  mask string is         :", maskParts[2])
                print(f'  zeros mask in binary is: {self.zerosMask:>036b}')
                print(f'  ones mask in binary is : {self.onesMask:>036b}')
            else:
                self.memLocList = []
                print("  line is a mem location")
                memParts = line.split()
                value = int(memParts[2])
                memParts = line.split("[")
                memParts2 = memParts[1].split("]")
                memLoc = memParts2[0]
                self.memLocList.append(int(memParts2[0]))
                print(f'memLocList[0] before | is: {self.memLocList[0]:>036b}')
                self.memLocList[0] = self.memLocList[0] | self.onesMask
                #self.memLocList[0] = self.memLocList[0] & self.zerosMask
                print(f'memLocList[0] after &| is: {self.memLocList[0]:>036b}')
                stringCount = 1
                tempLocList = []
                for c in reversed(self.currentMask):
                    if c == 'X':
                        for i, location in enumerate(self.memLocList):
                            self.memLocList[i] = location | stringCount
                            tempLocList.append(location & (~stringCount & self.maskAnd))
                        self.memLocList.extend(tempLocList)
                        tempLocList = []
                        print("stringCount is ", stringCount, "and loclist is", self.memLocList)
                    stringCount *= 2

                for location in self.memLocList:
                    print("    change location", location, "by", value)
                    self.memoryLocations[location] = value

    def printLocations(self):
        for loc in self.memoryLocations.keys():
            print ("location:", loc, "value:", self.memoryLocations[loc])

    def sumLocations(self):
        total = 0
        for loc in self.memoryLocations.keys():
            print ("location:", loc, "value:", self.memoryLocations[loc])
            total += self.memoryLocations[loc]
        print("Total is:", total)

if __name__ == '__main__':

    instructions = DockingData()

    instructions.processInput()
    instructions.printLocations()
    instructions.sumLocations()

