import fileinput

class JoltAdapters():
    def __init__(self):
        self.adapterList =[0]
        self.oneJolt = 0
        self.threeJolts = 0
        self.memoization = [0]

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
        for i in range(len(self.adapterList), -1, -1):
            print("i is: ", i)


if __name__ == '__main__':
    adapters = JoltAdapters()

    adapters.read_adapters()
    adapters.print_adapters()
    adapters.check_jolts()