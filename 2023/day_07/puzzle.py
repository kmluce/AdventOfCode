from utils.debugging import PrintDebug


def card_hand_type(hand: str):
    hand_list = [*hand]
    unique_hand_values = set(hand_list)
    return calc_hand_type(hand_list, unique_hand_values)


def calc_hand_type(hand_list, unique_hand_values):
    sorted_counts = [hand_list.count(x) for x in list(unique_hand_values)]
    sorted_counts.sort(reverse=True)
    if sorted_counts == [5]:
        hand_type = 7
    elif sorted_counts == [4, 1]:
        hand_type = 6
    elif sorted_counts == [3, 2]:
        hand_type = 5
    elif sorted_counts == [3, 1, 1]:
        hand_type = 4
    elif sorted_counts == [2, 2, 1]:
        hand_type = 3
    elif sorted_counts == [2, 1, 1, 1]:
        hand_type = 2
    else:
        hand_type = 1
    return hand_type


def joker_card_hand_type(hand: str):
    hand_list = [*hand]
    unique_hand_values = set(hand_list)
    candidate_card_values = []
    if 'J' in unique_hand_values:
        for sub in unique_hand_values:
            if sub == 'J':
                pass
            else:
                candidate_hand = hand.replace('J', sub)
                candidate_card_values.append(calc_hand_type([*candidate_hand], unique_hand_values.difference('J')))
    candidate_card_values.append(calc_hand_type(hand_list, unique_hand_values))
    return max(candidate_card_values)


def card_value(face: str):
    if face.isnumeric():
        return int(face)
    elif face == 'T':
        return 10
    elif face == 'J':
        return 11
    elif face == 'Q':
        return 12
    elif face == 'K':
        return 13
    elif face == 'A':
        return 14


def joker_card_value(face: str):
    if face.isnumeric():
        return int(face)
    elif face == 'T':
        return 10
    elif face == 'J':
        return 1
    elif face == 'Q':
        return 12
    elif face == 'K':
        return 13
    elif face == 'A':
        return 14


def card_hand_value(hand: str):
    hand_list = [*hand]
    hand_value = 0
    for card in hand_list:
        hand_value = hand_value * 100 + card_value(card)
    return hand_value


def joker_card_hand_value(hand: str):
    hand_list = [*hand]
    hand_value = 0
    for card in hand_list:
        hand_value = hand_value * 100 + joker_card_value(card)
    return hand_value


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.hands = []
        self.hand_values = {}
        self.hands_sorted = []

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
                    hand, value = line.split()
                    self.hands.append(hand)
                    self.hand_values[hand] = int(value)
                else:
                    pass

    def sort_cards(self):
        self.hands_sorted = sorted(self.hands, key=card_hand_value)
        print(self.hands_sorted)
        self.hands_sorted = sorted(self.hands_sorted, key=card_hand_type)
        print(self.hands_sorted)

    def joker_sort_cards(self):
        self.hands_sorted = sorted(self.hands, key=joker_card_hand_value)
        print(self.hands_sorted)
        self.hands_sorted = sorted(self.hands_sorted, key=joker_card_hand_type)
        print(self.hands_sorted)

    def solve(self):
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            self.sort_cards()
            return sum([(i + 1) * self.hand_values[j] for i, j in enumerate(self.hands_sorted)])
        else:
            self.joker_sort_cards()
            return sum([(i + 1) * self.hand_values[j] for i, j in enumerate(self.hands_sorted)])
