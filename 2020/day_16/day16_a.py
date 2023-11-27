import fileinput

class TicketTranslation():
    def __init__(self):
        self.validValueMap = {}
        self.fieldRanges = []
        self.fieldNames =[]
        self.myTicket =[]
        self.validTicketMap = []
        self.columnToNameMap = {}
        self.noColumns = 0
        self.matchMatrix = []
        self.matchSum=[]

    def inputFieldRanges(self, line):
        line = line.rstrip()
        fields = line.split(':')
        self.fieldNames.append(fields[0])
        self.fieldRanges.append({})
        myRanges = fields[1].split()
        print(myRanges)
        for i in [0, 2]:
            rangeBounds = myRanges[i].split('-')
            for j in range(int(rangeBounds[0]), int(rangeBounds[1]) + 1):
                #print("adding", j, "to valid numbers list")
                self.validValueMap[j] = True
                self.fieldRanges[-1][j] = True
        print(self.fieldNames)
        print(self.fieldRanges)

    def inputMyTicket(self,line):
        if 'your' not in line:
            self.myTicket = line.split(',')
            self.myTicket = [ int(i) for i in self.myTicket]
        self.noColumns = len(self.myTicket)


    def inputValidTickets(self, line):
        allFieldsValid = True
        if "nearby" not in line:
            line = line.rstrip()
            print(line)
            fieldVals = line.split(',')
            fieldVals = [int(i) for i in fieldVals]
            for field in fieldVals:
                if field not in self.validValueMap:
                    print("field", field, "is invalid, marking invalid")
                    allFieldsValid = False
                    break
            if allFieldsValid:
                self.validTicketMap.append(fieldVals)

    def printValidTickets(self):
        for row in self.validTicketMap:
            print(row)

    def readTicketInfo(self):
        totalInvalid = 0
        fileSegment = 0
        for line in fileinput.input():
            if not line.strip():
                fileSegment += 1
            elif fileSegment == 0:
                self.inputFieldRanges(line)
            elif fileSegment == 1:
                self.inputMyTicket(line)
            elif fileSegment == 2:
                self.inputValidTickets(line)

    def determineFieldNames(self):
        self.matchMatrix = []
        impossibleTotal= 0
        for i, fieldmap in enumerate(self.fieldRanges):
            self.matchMatrix.append([])
            self.matchMatrix[i] = [1 for i in range(len(self.validTicketMap[0]))]
        for ticIndex, ticket in enumerate(self.validTicketMap):
            for index, fieldmap in enumerate(self.fieldRanges):
                for column, colVal in enumerate(self.validTicketMap[ticIndex]):
                    #print("  testing row", ticIndex, "column", column, "value", colVal, "against", self.fieldNames[index] )
                    if colVal in fieldmap:
                        #print("    found")
                        #if column not in self.matchMatrix[index]:
                        #    self.matchMatrix[index][column] = 1
                        pass
                    else:
                        print("    NOT found")
                        print("    incorrect value", colVal, "marking column", column, "as impossible for", index, self.fieldNames[index])
                        impossibleTotal += 1
                        print("    impossible total is:", impossibleTotal)
                        self.matchMatrix[index][column]  = 0
        self.printMatchMatrixAndSum()
        self.matchSum = [0 for i in range(self.noColumns)]
        for row, ticket in enumerate(self.matchMatrix):
            for col, value in enumerate(self.matchMatrix[row]):
                self.matchSum[col] += self.matchMatrix[row][col]

        self.printMatchMatrixAndSum()

        while sum(self.matchSum) > len(self.matchSum):
            for col, val in enumerate(self.matchSum):
                if val == 1:
                    correctRow = self.findValidRow(col)
                    for i, value in enumerate(self.matchMatrix[correctRow]):
                        self.printMatchMatrixAndSum()
                        if i == col:
                            pass
                        else:
                            if self.matchMatrix[correctRow][i] == 1:
                                self.matchMatrix[correctRow][i] = 0
                                self.matchSum[i] -= 1

    def populateColumnMap(self):
        for i, row in enumerate(self.matchMatrix):
            for j, val in enumerate(self.matchMatrix[i]):
                if val == 1:
                    self.columnToNameMap[j] = self.fieldNames[i]
        print(self.columnToNameMap)



    def printMatchMatrixAndSum(self):
        print("Match Matrix and sum:")
        for i, row in enumerate(self.matchMatrix):
            print(self.fieldNames[i], row)
        print(self.matchSum)
        print(" ")

    # Find the row that has this column listed as valid (True)
    def findValidRow(self, col):
        for i, row in enumerate(self.matchMatrix):
            if row[col] == 1:
                return i
        return -1

    def findFinalValue(self):
        finalTotal = 1
        for col, val in enumerate(self.myTicket):
            print("checking column name for", self.columnToNameMap[col])
            if self.columnToNameMap[col].startswith('departure'):
                finalTotal *= self.myTicket[col]
        print("Final Total is", finalTotal)


if __name__ == '__main__':
    ticketNotes = TicketTranslation()

    ticketNotes.readTicketInfo()
    ticketNotes.printValidTickets()
    ticketNotes.determineFieldNames()
    ticketNotes.populateColumnMap()
    ticketNotes.findFinalValue()