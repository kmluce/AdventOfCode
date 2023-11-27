import fileinput
import string

class EncodingError:
    def __init__(self):
        self.dataStack =[]
        self.fullDataList = []
        self.preambleSize = 25
        self.encryptionBreak = -1

    def setRollingSize(self, size):
        self.preambleSize = size

    def pushOntoStack(self, newVal):
        self.fullDataList.append(newVal)
        print(self.fullDataList[-self.preambleSize:])

    def checkValidData(self, checkVal):
        if len(self.fullDataList) < self.preambleSize:  # still reading preamble, no check possible
            return True
        firstStackIndex = len(self.fullDataList) - self.preambleSize
        for i in range (firstStackIndex, len(self.fullDataList)):
            for j in range (firstStackIndex, i):
                if (self.fullDataList[i] + self.fullDataList[j]) == checkVal:
                    return True
        self.encryptionBreak = checkVal
        return False

    def findWeakness(self):
        sumTotal = 0
        currNum = 0

        if self.encryptionBreak == -1:
            print("ERROR: can't find the encryption weakness before checking valid data.")
            return -1
        for firstNum in range(0, len(self.fullDataList)):
            currNum = firstNum
            while sumTotal < self.encryptionBreak:
                sumTotal += self.fullDataList[currNum]
                currNum += 1
            if sumTotal == self.encryptionBreak:
                print("solution is indexes ", firstNum, " through ", currNum -1)
                print(self.fullDataList[firstNum:currNum])
                solutionSet = self.fullDataList[firstNum:currNum]
                solutionSet.sort()
                print("Solution sum is ", solutionSet[0] + solutionSet[-1])
                return
            else:
                sumTotal=0



if __name__ == '__main__':
    code = EncodingError()

    code.setRollingSize(25)
    for line in fileinput.input():
        line = line.rstrip()
        print(line)
        if not code.checkValidData(int(line)):
            print("First invalid value is: ", int(line))
            break
        code.pushOntoStack(int(line))
    code.findWeakness()
