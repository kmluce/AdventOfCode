class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.calledNumbers = []
        self.currBingo = []
        self.allBingos = []
        self.CALLED = -1
        self.new_list = []

    def parse(self):
        with open(self.fileName) as file:
            first_line = True
            for line in file:
                line = line.rstrip()
                line = line.lstrip()
                if first_line:
                    self.calledNumbers = line.split(',')
                    self.calledNumbers = [int(x) for x in self.calledNumbers]
                    first_line = False
                else:
                    if line:
                        #                        print(" line is", line)
                        bingoes = line.split()
                        bingoes = [int(x) for x in bingoes]
                        self.currBingo.append(bingoes)
                    #                        print("    adding current split line line", line.split())
                    else:
                        if self.currBingo:
                            self.allBingos.append(self.currBingo)
                            self.currBingo = []
        self.allBingos.append(self.currBingo)
        x: object
        # self.allBingos = [ x for x in self.allBingos if x]
        #self.print_bingo()

    def print_bingo(self):
        print("called numbers are", self.calledNumbers)
        print("bingos are:")
        # print(self.allBingos)
        for s in self.allBingos:
            print(s)
            print("xx")

    def mark_called(self, my_call):
        self.new_list = [[[-1 if b == my_call else b for b in a] for a in c] for c in self.allBingos]
        self.allBingos = self.new_list

    # returns the index of the winning bingo card, or -1 if none is currently winning
    def check_win(self) -> int:
        for bingo_card in self.allBingos:
            curr_index = self.allBingos.index(bingo_card)
            # print("this is bingo card #", curr_index)
            for line in bingo_card:
                # print(line)
                remaining_nums = [x for x in line if x != -1]
                if not remaining_nums:
                    return curr_index
            for j in range(len(bingo_card[0])):
                uncalled_nos = False
                for i in range(len(bingo_card)):
                    if bingo_card[i][j] != -1:
                        uncalled_nos = True
                        break
                if not uncalled_nos:
                    return curr_index
        return -1

    def sum_bingo(self, bingo_index: int) -> int:
        bingo_sum = 0
        for line in self.allBingos[bingo_index]:
            bingo_sum += sum([int(x) for x in line if x != -1])
        return bingo_sum

    def solvea(self):
        winning_no = -1
        result = -1
        for x in self.calledNumbers:
            self.mark_called(x)
            result = self.check_win()
            if result != -1:
                winning_no = x
                break
        #print("matching bingo card is #", result, ",winning_no is", winning_no)
        card_sum = self.sum_bingo(result)
        #print("card sum is ", card_sum)
        #self.print_bingo()
        return card_sum * winning_no

    def solveb(self):
        global result
        winning_no = -1
        # iterating through all of the bingo numbers called as x
        for x in self.calledNumbers:
            result = -1
            # print ("marking cards for bingo call", x)
            self.mark_called(x)
            result = self.check_win()
            if len(self.allBingos) == 1 and result != -1:
                winning_no=x
                break
            while result != -1:
                winning_no = x
                if len(self.allBingos) == 1:
                    break
                else:
                    self.allBingos.pop(result)
                    result = self.check_win()
                    #print("popped a card, number of cards remaining is:", len(self.allBingos))
        #print("number of cards remaining is:", len(self.allBingos))
        #print("matching bingo card is #", result, ",winning_no is", winning_no)
        card_sum = self.sum_bingo(result)
        #print("card sum is ", card_sum)
        #self.print_bingo()
        return card_sum * winning_no
