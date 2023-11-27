import fileinput

class RambunctiousRecitation():
    def __init__(self):
        self.iteration = 0
        self.lastUsed = {}
        self.lastNum = 0
        self.newNum = 0

    def startingNumbers(self, line):
        self.iteration = 0
        self.lastUsed = {}
        self.lastNum = 0
        self.newNum = 0
        startNums = [ int(i) for i in line.split(',')]
        for i in startNums[0:-1]:
            i = int(i)
            self.iteration += 1
            self.lastNum = i
            print("starting number", self.iteration, "is", i)
            self.lastUsed[i] = self.iteration
        self.playGame(startNums[-1])

    def playGame(self, startNum):
        print("starting number is", startNum)
        self.lastNum = startNum
        #while self.iteration < 2019:
        while self.iteration < 29999999:
            self.iteration += 1
            self.newNum = self.lastNum
            #print("  iterating with last number", self.lastNum)
            if self.lastNum in self.lastUsed and self.lastUsed[self.lastNum] < self.iteration:
                self.newNum = self.iteration - self.lastUsed[self.lastNum]
                self.lastUsed[self.lastNum] = self.iteration
                self.lastNum = self.newNum
            else:
                self.lastUsed[self.lastNum] = self.iteration
                self.lastNum = 0
            #print("     new number is ", self.lastNum)
        print("final number is:", self.lastNum)


    def processFile(self):
        for line in fileinput.input():
            line = line.rstrip()
            print("line:", line)
            self.startingNumbers(line)

if __name__ == '__main__':
    game1 = RambunctiousRecitation()
    game1.processFile()