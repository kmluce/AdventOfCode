import fileinput

def parse_line(line):
    splitLine = line.split()
    print(splitLine)
    srrange = splitLine[0].split('-')
    return [ int(srrange[0]), int(srrange[1]), splitLine[1][0], splitLine[2] ]

def check_string(myArgs):
    low = myArgs[0]
    high = myArgs[1]
    matchChar = myArgs[2]
    matchString = myArgs[3]

    if matchString[low -1 ] == matchChar or matchString[high -1] == matchChar:
        if not (matchString[low - 1] == matchChar and matchString[high - 1] == matchChar):
            return True
    return False

if __name__ == '__main__':
    validCount = 0
    for line in fileinput.input():
        line = line.rstrip()
        parsedLine = parse_line(line)
        print(" rangelow: ", parsedLine[0], " rangehigh: ", parsedLine[1], " char: ", parsedLine[2],
              " string: ", parsedLine[3])
        if check_string(parsedLine):
            validCount += 1
    print("Number of valid passwords is: ", validCount)