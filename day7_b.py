import fileinput
import string
import re
from collections import defaultdict

def check_a_graph_path(bagType, matchType, graphDict):
    testList = []

    #print("  checking graph for ", bagType, " matching ", matchType)
    testList.append(bagType)
    testList.append(matchType)
    #print(testList)
    if bagType == matchType:
        return True
    elif any('no other' in v for v in graphDict[bagType]):
        return False
    for nextBag in graphDict[bagType]:
        if(check_a_graph_path(nextBag, matchType, graphDict)):
            return True


if __name__ == '__main__':
    myGraph = defaultdict(list)
    graphIndex = {}
    numPaths=0

    for line in fileinput.input():
        line = line.rstrip()
        splitLine = re.split(" *bags contain[0-9 ]*|[0-9 ]*bags?[ ,.0-9]*", line)
        print(splitLine)

        for i in range(1, len(splitLine)):
            if splitLine[i]:
                myGraph[splitLine[0]].append(splitLine[i])

    print(myGraph.items())
    print(check_a_graph_path('bright white', 'shiny gold', myGraph))
    print(check_a_graph_path('light red', 'shiny gold', myGraph))
    print(check_a_graph_path('dark olive', 'shiny gold', myGraph))
    for key in myGraph.keys():
        if key != 'shiny gold':
            if check_a_graph_path(key,'shiny gold', myGraph):
                print("FOUND path for ", key)
                numPaths += 1
            else:
                print("DID NOT FIND a path for ", key)

    print("found ", numPaths, " total paths.")