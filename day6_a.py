import fileinput
import string

def total_group(myGroup):
    thisTotal = 0

    for i in range(len(myGroup)):
        thisTotal += myGroup[i]

    print("   found total ", thisTotal)
    return(thisTotal)


if __name__ == '__main__':
    thisSum = 0
    groupTotals = []
    thisGroup = [0 for i in range(26)]

    for line in fileinput.input():
        print("  line: ", line)
        if line == "\n":
            groupTotals.append(total_group(thisGroup))
            thisGroup = [0 for i in range(26)]
        else:
            line = line.rstrip()
            for char in list(line):
                print("   char is ", char)
                charIndex = string.ascii_lowercase.index(char)
                print("   setting value of space ", charIndex, "to 1.")
                thisGroup[charIndex] = 1

    groupTotals.append(total_group(thisGroup))

    for i in range(len(groupTotals)):
        thisSum += groupTotals[i]

    print("sum is ", thisSum)