import fileinput
import string
import re
from collections import defaultdict

def check_total_bags(bagType, graphDict):
    print("  checking total bags for ", bagType)
    totalBags: int = 0

    for i in range(0, len(graphDict[bagType]), 2):
        if graphDict[bagType][i] == 0:
            return 1
        else:
            print("   totalBags is currently ", totalBags)
            print("   Adding ", graphDict[bagType][i], " bags of type ", graphDict[bagType][i+1], " to my ", bagType)
            bagResult = check_total_bags(graphDict[bagType][i+1],graphDict)
            print("    Bag Type ", graphDict[bagType][i+1], " retunred ", bagResult, " bags.")
            totalBags += (bagResult * graphDict[bagType][i] )

    return totalBags + 1

def check_a_graph_path(bagType, matchType, graphDict):
    testList = []

    print("  checking graph for ", bagType, " matching ", matchType)
    testList.append(bagType)
    testList.append(matchType)
    #print(testList)
    if bagType == matchType:
        print("    returning True because we're checking ", bagType)
        return True
    #elif any('no other' in v for v in graphDict[bagType]):
    #    print("    returning False because I found string no other")
    #    return False
    #for nextBag in graphDict[bagType]:
    for i in range(0, len(graphDict[bagType]), 2):
        print("  entry is ", graphDict[bagType][i], " and ", graphDict[bagType][i + 1])
        if graphDict[bagType][i] == 0:
            print('    Passing because an even value is 0')
        elif check_a_graph_path(graphDict[bagType][i + 1], matchType, graphDict):
            return True
    return False

if __name__ == '__main__':
    myGraph = defaultdict(list)
    graphIndex = {}
    numPaths=0

    for line in fileinput.input():
        line = line.rstrip()
        splitLine = re.split(" *bags contain|bags?[ ,.]*", line)
        print(splitLine)
        #numpat = re.compile('\d+')
        #lettpat = re.compile('[a-z]+[a-z ]*')

        for i in range(1, len(splitLine)):
            if splitLine[i]:
                numpat = re.findall("\d+", splitLine[i])
                if numpat:
                    myGraph[splitLine[0]].append(int(numpat[0]))
                else:
                    myGraph[splitLine[0]].append(0)
                lettPat = re.findall("[a-z]+[a-z ]*[a-z]", splitLine[i])
                #myGraph[splitLine[0]].append(splitLine[i])
                if lettPat:
                    myGraph[splitLine[0]].append(lettPat[0])

    print(myGraph.items())
    print("Basic testing:")
    print(check_a_graph_path('bright white', 'shiny gold', myGraph))
    print(check_a_graph_path('light red', 'shiny gold', myGraph))
    print(check_a_graph_path('dark olive', 'shiny gold', myGraph))
    print("Checking all paths now:")
    for key in myGraph.keys():
        if key != 'shiny gold':
            if check_a_graph_path(key,'shiny gold', myGraph):
                print("FOUND path for ", key)
                numPaths += 1
            else:
                print("DID NOT FIND a path for ", key)

    print("found ", numPaths, " total paths.")

    print("Shiny gold bags hold ", check_total_bags('shiny gold', myGraph)-1)