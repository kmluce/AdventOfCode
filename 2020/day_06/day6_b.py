import fileinput
import string

def total_group(numPeople,myGroup):
    thisTotal = 0

    for i in range(len(myGroup)):
        if myGroup[i] == peopleCount:
            thisTotal += 1

    print("   found total ", thisTotal)
    return(thisTotal)


if __name__ == '__main__':
    thisSum = 0
    groupTotals = []
    thisGroup = [0 for i in range(26)]
    peopleCount = 0

    for line in fileinput.input():
        print("  line: ", line)
        if line == "\n":
            print ("  totaling with peoplecount = ", peopleCount)
            groupTotals.append(total_group(peopleCount, thisGroup))
            thisGroup = [0 for i in range(26)]
            peopleCount = 0
        else:
            line = line.rstrip()
            peopleCount += 1
            for char in list(line):
                print("   char is ", char)
                charIndex = string.ascii_lowercase.index(char)
                print("   setting value of space ", charIndex, "to 1.")
                thisGroup[charIndex] += 1

    groupTotals.append(total_group(peopleCount, thisGroup))

    for i in range(len(groupTotals)):
        thisSum += groupTotals[i]

    print("sum is ", thisSum)