import fileinput
import re
import string

class OperationOrder():
    def __init__(self):
        self.operationStack = []
        self.currentLine = []
        self.currLeft = 0
        self.currRight = 0
        self.currOp = ''

    def print_stack(self):
        print(" Stack:", self.operationStack)

    def sum(self, left, right):
        return(int(left) + int(right))

    def multiply(self, left, right):
        return(int(left) * int(right))

    def add_token_to_stack(self, token):
        self.operationStack.append(token)
        self.print_stack()

    def process_stack(self):
        iterate = True
        while iterate == True:
            if len(self.operationStack) < 3:
                print("  stack length is less than 3, no operations possible")
                iterate = False
                break
            elif self.operationStack[-1] == '+' or self.operationStack[-1] == '-' or self.operationStack[-1] == '(':
                print("  most recent token is an operator, no operations possible")
                iterate = False
                break
            elif self.operationStack[-1] == ')':
                print("  most recent token is close paren, trying to close the paren")
                if self.operationStack[-3] == '(':
                    self.operationStack.pop()
                    value = self.operationStack.pop()
                    self.operationStack.pop()
                    self.operationStack.append(value)
                    self.print_stack()
            elif self.operationStack[-2] == '+':
                print("  next most recent token is +, adding")
                right = self.operationStack.pop()
                right = int(right)
                self.operationStack.pop()
                left = self.operationStack.pop()
                left = int(left)
                self.operationStack.append(self.sum(left, right))
                self.print_stack()
            elif self.operationStack[-2] == '*':
                print("  next most recent token is *, multiplying")
                right = self.operationStack.pop()
                right = int(right)
                self.operationStack.pop()
                left = self.operationStack.pop()
                left = int(left)
                self.operationStack.append(self.multiply(left, right))
                self.print_stack()
            else:
                iterate = False
                break


    def process_line(self, line):
        line = line.rstrip()
        print(line)
        line = re.sub('([()])', r' \1 ', line)
        print("line is:", line)
        fields = line.split()
        for token in fields:
            currToken = token
            print("processing token:", currToken)
            self.add_token_to_stack(currToken)
            self.process_stack()
        return self.operationStack.pop()

    def read_lines(self):
        total = 0
        for line in fileinput.input():
            line = line.rstrip()
            self.currentLine = line
            total += self.process_line(line)
            self.__init__()
        print("total value is", total)


if __name__ == '__main__':
    homework1 = OperationOrder()
    homework1.read_lines()
