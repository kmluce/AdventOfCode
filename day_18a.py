import fileinput

class OperationOrder():
    def __init__(self):
        self.operationStack = []
        self.currentLine = []
        self.currLeft = 0
        self.currRight = 0
        self.currOp = ''

    def printStack(self):
        print(" Stack:", self.operationStack)

    def sum(self, left, op, right):
        return(int(left) + int(right))

    def multiply(self, left, op, right):
        return(int(left) * int(right))

    def processLine(self, line):
        line = line.rstrip()
        print(line)
        fields = line.split()
        for token in fields:
            print("processing token:", token)
            if token == '+':
                self.operationStack.append(token)
                self.printStack()
            elif token == '*':
                self.operationStack.append(token)
                self.printStack()
            elif token == '(':
                self.operationStack.append(token)
                self.printStack()
            else:
                # must be a number
                token = int(token)
                if len(self.operationStack) >= 2:
                    if self.operationStack[-1] == '+':
                        self.currRight = token
                        self.currOp = self.operationStack.pop()
                        self.currLeft = self.operationStack.pop()
                        self.printStack()
                        print("  Preparing to add", self.currLeft, self.currOp, self.currRight)
                        self.operationStack.append(self.sum(self.currLeft, self.currOp, self.currRight))
                        self.printStack()
                    elif self.operationStack[-1] == '*':
                        self.currRight = token
                        self.currOp = self.operationStack.pop()
                        self.currLeft = self.operationStack.pop()
                        self.printStack()
                        print("  Preparing to add", self.currLeft, self.currOp, self.currRight)
                        self.operationStack.append(self.multiply(self.currLeft, self.currOp, self.currRight))
                        self.printStack()
                else:
                    self.operationStack.append(token)
                    self.printStack()

    def readLines(self):
        for line in fileinput.input():
            line = line.rstrip()
            self.currentLine = line
            self.processLine(line)


if __name__ == '__main__':
    homework1 = OperationOrder()
    homework1.readLines()
