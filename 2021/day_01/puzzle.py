def parse(lines):
    parsedList = []
    for x in lines:
        parsedList.append(int(x.strip()))
    print(parsedList)
    return parsedList

def solvea(data):
    totalIncrease=0
    totalNotIncrease=0
    totalEntries=0
    priorData=-1
    for x in data:
        totalEntries+=1
        if priorData == -1:
            #/14pass
            totalNotIncrease +=1
        else:
            if x >= priorData:
                totalIncrease += 1
                #print("  ", priorData, x, "(increased)", totalIncrease)
            else:
                totalNotIncrease += 1
                #print("  ", priorData, x, "(decreased)")
        priorData = x

    print("Total number of entries is", totalEntries, ", number of increases is", totalIncrease, "other is", totalNotIncrease)
    return totalIncrease

def solveb(data):
    totalIncrease=0
    totalNotIncrease=0
    totalEntries=0
    priorData= []
    windowSize=3
    for x in data:
        totalEntries+=1
        if len(priorData) < windowSize:
            #/14pass
            totalNotIncrease +=1
            priorData.append(x)
            #print("x is", x, "but window not big enough yet")
        else:
            priorData.append(x)
            #print("x is", x, "first window is", sum(priorData[0:windowSize]), "second is", sum(priorData[1:windowSize+1]) )
            if sum(priorData[1:windowSize +1]) > sum(priorData[0:windowSize]):
                totalIncrease += 1
                #print("  ", priorData, x, "(increased)", totalIncrease)
            else:
                totalNotIncrease += 1
                #print("  ", priorData, x, "(decreased)")
            priorData.pop(0)

    print("Total number of entries is", totalEntries, ", number of increases is", totalIncrease, "other is", totalNotIncrease)
    return totalIncrease