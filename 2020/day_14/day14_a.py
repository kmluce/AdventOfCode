import fileinput

class DockingData():
    def __init__(self):
        self.onesMask = 0
        self.zerosMaskComplement = 0
        self.zerosMask = 0
        self.memoryLocations = {}

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
                stringCount = 1
                for c in reversed(maskParts[2]):
                    if c == '0':
                        print("    character is 0, so adding", stringCount, "to zeros mask complement.")
                        self.zerosMaskComplement += stringCount
                    elif c == '1':
                        print("    character is 1, so adding", stringCount, "to ones mask.")
                        self.onesMask += stringCount
                    stringCount *= 2
                self.zerosMask = ~ self.zerosMaskComplement & 68719476735
                print("  Ones mask is:", self.onesMask)
                print("  zeros mask complement is:", self.zerosMaskComplement)
                print("  zeros mask is:", self.zerosMask)
                print("  mask string is         :", maskParts[2])
                print(f'  zeros mask in binary is: {self.zerosMask:>08b}')
                print(f'  ones mask in binary is : {self.onesMask:>08b}')
            else:
                print("  line is a mem location")
                memParts = line.split()
                value = int(memParts[2])
                memParts = line.split("[")
                memParts2 = memParts[1].split("]")
                memLoc = memParts2[0]
                print("    change location", memLoc, "by", value)
                result = value | self.onesMask
                result = result & self.zerosMask
                print("    result is", result)
                self.memoryLocations[memLoc] = result

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

