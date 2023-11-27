import fileinput

class JoltAdapters():
    def __init__(self):
        self.adapterList =[0]
        self.oneJolt = 0
        self.threeJolts = 0
        self.memoArray = [0]

    def read_adapters(self):
        for line in fileinput.input():
            line = line.rstrip()
            self.adapterList.append(int(line.rstrip()))
        self.adapterList.sort()
        self.adapterList.append(self.adapterList[-1] + 3)

    def print_adapters(self):
        print(self.adapterList)

    def check_jolts(self):
        for i in range(0, len(self.adapterList)-1):
            print("comparing ", self.adapterList[i], " versus ", self.adapterList[i+1])
            if self.adapterList[i+1] - self.adapterList[i] == 1:
                print(" difference is 1")
                self.oneJolt += 1
            elif self.adapterList[i+1] - self.adapterList[i] == 3:
                print(" difference is 3")
                self.threeJolts += 1

        print("One jolt transitions: ", self.oneJolt, " three jolt transitions: ", self.threeJolts)
        print("Product of one jolt and three jolt: ", self.oneJolt * self.threeJolts)

    def memoization(self):
        for i in range(len(self.adapterList) -1):
            self.memoArray.append(0)
        #print("setting memo array ", len(self.adapterList)-1, "to 1")
        self.memoArray[len(self.adapterList)-1] = 1
        #print(self.memoArray)
        for i in range(len(self.adapterList )-2, -1, -1):
            for j in range(i+1, i+4):
                if j >= len(self.adapterList):
                    pass
                else:
                    #print('checking for array indexes ', i, ",", j, "with values ", self.adapterList[i], ",", self.adapterList[j])
                    if (self.adapterList[j] - self.adapterList[i]) <= 3:
                        self.memoArray[i] += self.memoArray[j]
        print(self.adapterList)
        print(self.memoArray)
        return(self.memoArray[0])



if __name__ == '__main__':
    adapters = JoltAdapters()

    adapters.read_adapters()
    adapters.print_adapters()
    #adapters.check_jolts()
    print(adapters.memoization())