class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.lanternfish_ages = []
        self.lanternfish_count = []

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                self.lanternfish_ages = [int(x) for x in line.split(',')]
                self.lanternfish_count = [self.lanternfish_ages.count(x) for x in range(0, 7)]
        self.lanternfish_count.extend([0, 0])  # adding spaces for 7 and 8
        print("age list is:", self.lanternfish_ages)
        print("count list is:", self.lanternfish_count)


    def solvea(self, days):
        zeros = 0
        num_new_fish = 0
        updated_fish = []
        for i in range(days):
            #print("iteration", i)
            zeros = self.lanternfish_count.pop(0)
            self.lanternfish_count[6] += zeros
            self.lanternfish_count.append(zeros)
            #print("  sum is ", sum(self.lanternfish_count))
        return sum(self.lanternfish_count)

