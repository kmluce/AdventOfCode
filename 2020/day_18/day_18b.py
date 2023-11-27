import fileinput
import re
import string

class OperationOrder():
    def __init__(self):
        self.operationStack = []

    def print_stack(self):
        print(" Stack:", self.operationStack)

    def add_token_to_stack(self, token):
        self.operationStack.append(token)
        self.print_stack()

    def process_plusses(self):
        if len(self.operationStack) < 2:
            return
        index = 0
        self.print_stack()
        while index < len(self.operationStack):
            while len(self.operationStack) > index + 2 and  self.operationStack[index + 1] == '+':
                print ("checking for addition on index", index)
                if isinstance(self.operationStack[index], (int, float, complex)) and not isinstance(self.operationStack[index], bool):
                    if isinstance(self.operationStack[index+2], (int, float, complex)) and not isinstance(self.operationStack[index+2], bool):
                        print("  adding", self.operationStack[index], "and", self.operationStack[index+2])
                        self.operationStack[index] = self.operationStack[index] + self.operationStack[index + 2]
                        del self.operationStack[index+1:index+3]
                        self.print_stack()
                    else:
                        break
                else:
                    break
            index += 1

    def process_multiplication(self):
        if len(self.operationStack) < 2:
            return
        index = 0
        self.print_stack()
        while index < len(self.operationStack):
            while len(self.operationStack) > index + 2 and self.operationStack[index + 1] == '*':
                print ("checking for multiplicaiton on index", index)
                if isinstance(self.operationStack[index], (int, float, complex)) and not isinstance(self.operationStack[index], bool):
                    if isinstance(self.operationStack[index+2], (int, float, complex)) and not isinstance(self.operationStack[index+2], bool):
                        print("  multiplying", self.operationStack[index], "and", self.operationStack[index+2])
                        self.operationStack[index] = self.operationStack[index] * self.operationStack[index + 2]
                        del self.operationStack[index+1:index + 3]
                        self.print_stack()
                    else:
                        break
                else:
                    break
            index += 1

    def find_matching_paren(self, index):
        if self.operationStack[index] != '(':
            print("ERROR:  trying to find matching paren when there's no paren")
            return
        else:
            parenCount = 0
            for i, item in enumerate(self.operationStack[index:]):
                print("   matchingParen: checking index", i, "item", item)
                if item == '(':
                    parenCount += 1
                elif item == ')':
                    parenCount -= 1
                    if parenCount == 0:
                        return i
        return -1

    def process_parens(self):
        if len(self.operationStack) < 2:
            return
        index = 0
        self.print_stack()
        while len(self.operationStack) > index + 2 and index < len(self.operationStack):
            while self.operationStack[index] == '(':
                print ("checking for parens on index", index)
                if self.operationStack[index +2] == ')':
                    print("  removing parens")
                    del self.operationStack[index +2]
                    del self.operationStack[index]
                    self.print_stack()
                else:
                    subline = OperationOrder()
                    closeParen = self.find_matching_paren(index)
                    firstCloseParen = self.operationStack.index(')', index)
                    holdString = self.operationStack[index:closeParen+index +1]
                    print (" close parens index is", closeParen)
                    print (" parens is", self.operationStack[index:closeParen + index + 1])
                    if closeParen != -1:
                        for currToken in self.operationStack[index+1:closeParen+index]:
                            subline.add_token_to_stack(currToken)
                        parenVal = subline.process_line_repeatedly()
                        self.print_stack()
                        print("replacing", holdString, "with", parenVal)
                        self.operationStack[index] = parenVal
                        del self.operationStack[index+1:closeParen+index+1]
                        self.print_stack()
                    break
            index += 1

    def cast_to_int(self):
        for i, token in enumerate(self.operationStack):
            if token == '+':
                pass
            elif token == '*':
                pass
            elif token == '(':
                pass
            elif token == ')':
                pass
            else:
                self.operationStack[i] = int(token)


    def process_line_repeatedly(self):
        while len(self.operationStack) > 1:
            print("stack length is currently", len(self.operationStack))
            self.process_parens()
            self.process_plusses()
            self.process_multiplication()
        return self.operationStack[0]

    def read_lines(self):
        total = 0
        for line in fileinput.input():
            line = line.rstrip()
            print(line)
            line = re.sub('([()])', r' \1 ', line)
            print("line is:", line)
            self.operationStack = line.split()
            self.cast_to_int()
            total += self.process_line_repeatedly()
            self.__init__()
        print("total value is", total)


if __name__ == '__main__':
    homework1 = OperationOrder()
    homework1.read_lines()
