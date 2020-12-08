import fileinput
import string

def import_code(programList):
    for line in fileinput.input():
        line = line.rstrip()
        print(line)
        programList.append(line)

def execute_program(programList):
    accumulator = 0

    currStep = 0
    executedSteps={}
    while currStep < len(programList):
        print("step is ", currStep, ": ", programList[currStep], " accumulator is ", accumulator)
        if currStep in executedSteps.keys():
            print("this step has been executed already.  Returning with ", accumulator)
            return accumulator
        executedSteps[currStep] = True
        parsedStep = programList[currStep].split()
        print("parsedStep is ", parsedStep)
        if parsedStep[0] == 'nop':
            currStep += 1
        elif parsedStep[0] == 'acc':
            accumulator += int(parsedStep[1])
            currStep += 1
        elif(parsedStep[0]) == 'jmp':
            currStep += int(parsedStep[1])
        else:
            currStep += 1

if __name__ == '__main__':
    code = []

    import_code(code)
    print(code)
    accum = execute_program(code)
    print("Final accumulator value is: ", accum)