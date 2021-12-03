
class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.diagnostics = []
        self.total_ones=[]
        self.gamma_binary = ""
        self.gamma = 0
        self.epsilon_binary = ""
        self.epsilon = 0
        self.num_diagnostics = 0
        self.co_diagnostics = []
        self.og_diagnostics = []
        self.tmp_diagnostics = []
        self.tmp_totaldigits = []
        self.co2 = 0
        self.og = 0

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                self.diagnostics.append(line)
        self.num_diagnostics = len(self.diagnostics)

    def solvea(self):
        self.total_ones = len(self.diagnostics[0]) * [0]
        for binval in self.diagnostics:
            for x in range(len(binval)):
                if int(binval[x]) == 1:
                    self.total_ones[x] += 1
        print("bin total is", self.total_ones)
        half = self.num_diagnostics / 2
        print("half is", half)
        for x in range(len(self.total_ones)):
            if self.total_ones[x] > half:
                self.gamma_binary += "1"
                self.epsilon_binary += "0"
            else:
                self.gamma_binary += "0"
                self.epsilon_binary += "1"
        print("in binary, gamma is", self.gamma_binary, "and epsilon is", self.epsilon_binary)
        self.gamma = int(self.gamma_binary, 2)
        self.epsilon = int(self.epsilon_binary, 2)

        return self.gamma * self.epsilon

    def update_total_digits(self):
        self.tmp_totaldigits = (len(self.tmp_diagnostics[0])) * [0]
        for binval in self.tmp_diagnostics:
            for x in range(len(binval)):
                if int(binval[x]) == 1:
                    self.tmp_totaldigits[x] += 1

    def solveb(self):
        self.tmp_diagnostics = self.diagnostics
        self.update_total_digits()
        half = len(self.tmp_diagnostics) / 2
        for x in range(len(self.tmp_totaldigits)):
            print("total_digits is", self.tmp_totaldigits)
            if self.tmp_totaldigits[x]  >= half:
                keep_val = "1"
            else:
                keep_val = "0"
            print("keep value for digit", x, "is", keep_val)
            for diagnostic in self.tmp_diagnostics:
                print("considering value", x, "in", diagnostic)
                if diagnostic[x] != keep_val:
                    print("pruning string")
                    self.tmp_diagnostics = [value for value in self.tmp_diagnostics if value != diagnostic]
                print("diagnostics value is", self.tmp_diagnostics)
            if len(self.tmp_diagnostics) == 1:
                break
            self.update_total_digits()
            half = len(self.tmp_diagnostics) / 2
        print("there can be only one, and it is", self.tmp_diagnostics)
        self.og = int(self.tmp_diagnostics[0], 2)
        print("oxygen generator is", self.og)
        self.tmp_diagnostics = self.diagnostics
        self.update_total_digits()
        half = len(self.tmp_diagnostics) / 2
        for x in range(len(self.tmp_totaldigits)):
            print("total_digits is", self.tmp_totaldigits)
            if self.tmp_totaldigits[x]  < half:
                keep_val = "1"
            else:
                keep_val = "0"
            print("keep value for digit", x, "is", keep_val)
            for diagnostic in self.tmp_diagnostics:
                print("considering value", x, "in", diagnostic)
                if diagnostic[x] != keep_val:
                    print("pruning string")
                    self.tmp_diagnostics = [value for value in self.tmp_diagnostics if value != diagnostic]
                print("diagnostics value is", self.tmp_diagnostics)
            if len(self.tmp_diagnostics) == 1:
                break
            self.update_total_digits()
            half = len(self.tmp_diagnostics) / 2
        print("there can be only one, and it is", self.tmp_diagnostics)
        self.co2 = int(self.tmp_diagnostics[0], 2)
        print("CO2 is", self.co2)

        return self.og * self.co2