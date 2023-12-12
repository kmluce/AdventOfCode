from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.total_points = 0
        self.cards_owned = []
        self.card_copies = []
        self.num_cards_won_round = []
        self.list_cards_won_round = []

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    def parse(self):

        with open(self.fileName) as file:
            for line in file:
                if line.rstrip():
                    line = line.rstrip()
                    first_parsing_pass = line.split(':')
                    second_parsing_pass = first_parsing_pass[1].split('|')
                    winning_numbers = set([int(x) for x in second_parsing_pass[0].split()])
                    my_numbers = set([int(x) for x in second_parsing_pass[1].split()])
                    if winning_numbers.intersection(my_numbers):
                        self.total_points += pow(2, len(winning_numbers.intersection(my_numbers)) - 1)
                        self.card_copies.append(1)
                        self.num_cards_won_round.append(len(winning_numbers.intersection(my_numbers)))
                    else:
                        self.card_copies.append(1)
                        self.num_cards_won_round.append(0)
                else:
                    pass

    def calculate_cards_owned(self):
        self.list_cards_won_round = [None] * (len(self.num_cards_won_round))
        self.debug.print(1, "")
        for index, num_cards in reversed(list(enumerate(self.num_cards_won_round))):
            self.debug.print(3, f"card {index} won {num_cards} cards")
            self.list_cards_won_round[index] = [index]
            for i in range(0, num_cards):
                self.list_cards_won_round[index].extend(self.list_cards_won_round[index + i + 1])
        self.debug.print(2, f"{self.list_cards_won_round}")
        return len([x for sublist in self.list_cards_won_round for x in sublist])

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            return self.total_points
        else:
            return self.calculate_cards_owned()
