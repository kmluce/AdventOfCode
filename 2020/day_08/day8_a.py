import fileinput
import string

class HandheldExecution:
    def __init__(self):
        self.programList =[]
        self.executedSteps = {}
        self.accumulator = 0
        self.currStep=0
        self.loop = False
        for line in fileinput.input():
            line = line.rstrip()
            print(line)
            self.programList.append(line)

    def step(self, instruction, arguments=None):
        self.executedSteps[self.currStep] = True
        if instruction == 'nop':
            self.currStep += 1
        if instruction  == 'acc':
            self.accumulator += arguments[0]
            self.currStep += 1
        if instruction == 'jmp':
            self.currStep += arguments[0]

    def execute_program(self):
        while self.currStep < len(self.programList):
            print("step is ", self.currStep, ": ", self.programList[self.currStep], " accumulator is ", self.accumulator)
            if self.currStep in self.executedSteps.keys():
                print("this step has been executed already. Returning with accumulator ", self.accumulator)
                return self.accumulator
            parsedStep = self.programList[self.currStep].split()
            print("parsedStep is ", parsedStep)
            instructionList = [ int(parsedStep[1]) ]
            self.step(parsedStep[0], instructionList)

    def get_next_nop_jmp(self, index):
        for i in range (index + 1, len(self.programList)):
            if 'nop' in self.programList[i] or 'jmp' in self.programList[i]:
                return i
        return -1

    def fix_program(self):
        testedLines = -1
        testedThisPass = False
        totalRuns = 0
        while testedLines < len(self.programList) and totalRuns < len(self.programList):
            nextTest = self.get_next_nop_jmp(testedLines)
            print("Starting program execution, run ", totalRuns, " with ", testedLines, " lines tested and next test ", nextTest)
            totalRuns += 1
            while self.currStep < len(self.programList):
                print("  step is ", self.currStep, ": ", self.programList[self.currStep], " accumulator is ",
                      self.accumulator)
                if self.currStep in self.executedSteps.keys():
                    print("  this step has been executed already. Returning with accumulator ", self.accumulator)
                    if testedThisPass == False:
                        testedLines += 1
                    testedThisPass = False
                    self.currStep = 0
                    self.accumulator = 0
                    self.executedSteps.clear()
                    break
                parsedStep = self.programList[self.currStep].split()
                print("  parsedStep is ", parsedStep)
                instructionList = [ int(parsedStep[1]) ]
                if parsedStep[0] == 'nop' and nextTest == self.currStep and testedThisPass == False:
                    print("  Swapping out nop and swapping in jmp")
                    testedThisPass = True
                    testedLines = self.currStep
                    self.step('jmp', instructionList)
                elif parsedStep[0] == 'jmp' and nextTest == self.currStep and testedThisPass == False:
                    print("  Swapping out jmp and swapping in nop")
                    testedThisPass = True
                    testedLines = self.currStep
                    self.step('nop', instructionList)
                else:
                    self.step(parsedStep[0], instructionList)
            if self.currStep == len(self.programList):
                return self.accumulator



if __name__ == '__main__':
    code = HandheldExecution()

    print("Next jmp nop from -1 is", code.get_next_nop_jmp(-1))
    print("Next jmp nop from 0 is", code.get_next_nop_jmp(0))
    print("Next jmp nop from 1 is", code.get_next_nop_jmp(1))
    print("Next jmp nop from 3 is", code.get_next_nop_jmp(3))
    print("Next jmp nop from 5 is", code.get_next_nop_jmp(5))
    print("Next jmp nop from 8 is", code.get_next_nop_jmp(8))
    accum = code.fix_program()
    print("Final accumulator value is: ", accum)