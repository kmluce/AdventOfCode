import fileinput
import string

class EncodingError:
    def __init__(self):
        self.dataList =[]
        self.preambleSize = 25

    def setRollingSize(self, size):
        self.preambleSize = size

    def pushOntoStack(self, newVal):
        self.dataList.append(newVal)
        if len(self.dataList) > self.preambleSize:
            self.dataList.pop(0)
        print(self.dataList)

    def checkValidData(self, checkVal):
        if len(self.dataList) < self.preambleSize:  # still reading preamble, no check possible
            return True
        for i in range (0,len(self.dataList)):
            for j in range (0, i):
                if (self.dataList[i] + self.dataList[j]) == checkVal:
                    return True
        return False


if __name__ == '__main__':
    code = EncodingError()

    code.setRollingSize(25)
    for line in fileinput.input():
        line = line.rstrip()
        print(line)
        if not code.checkValidData(int(line)):
            print("First invalid value is: ", int(line))
            exit(0)
        code.pushOntoStack(int(line))
