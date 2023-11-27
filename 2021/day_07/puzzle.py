from statistics import mean


class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.crab_locations = []

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                self.crab_locations = [int(x) for x in line.split(',')]

    def solvea(self):
        # I swear I wasn't trying to code golf, list comprehensions are just fun.
        # this creates a one-dimensional array where the index is the possible x location
        # and the value is the sum of absolute differences between the values in
        # self.crab_locations and that possible x location -- so, the total cost to move there.
        # It then returns the minimum of that array.
        return min([sum([abs(ele - x) for ele in self.crab_locations]) for x in range(max(self.crab_locations))])

    def solveb(self):
        # this is the prior list comprehension modified per part II of the problem.
        # since the cost calculations change so that the distance to move N spaces is
        # sum of 1..N, we use the (n(n+1))/2 formula for that sum.
        return (min([sum([((abs(ele - x) * (abs(ele - x) + 1)) / 2) for ele in self.crab_locations]) for x in
                     range(max(self.crab_locations))]))
