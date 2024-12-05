from utils.debugging import PrintDebug


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.rules = []
        self.pages_list = []
        self.pages_dict = {}
        self.page_sum = 0

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
                    if '|' in line:
                        first, last = line.split('|')
                        self.rules.append([int(first), int(last)])
                    else:
                        self.debug.print(3, f"rule list looks like: {self.rules}")
                        self.pages_dict = {}
                        tmp_line = line.split(',')
                        self.debug.print(3, f"tmp_line looks like: {tmp_line}")
                        self.pages_list.append([int(x) for x in tmp_line])
                        for idx, i in enumerate(self.pages_list[-1]):
                            self.debug.print(3, f"in loop, i is {i}, and idx is {idx}")
                            self.pages_dict[i] = idx
                        self.check_rules_a(self.pages_dict, self.pages_list[-1])
                else:
                    pass
            pass

    def check_rules_a(self, pages_dict, page_list):
        self.debug.print(3, f"check_rules_a:  rule list looks like: {self.rules}")
        rule_follower = True
        for page in pages_dict.keys():
            self.debug.print(3, f"generating rule list for page: {page}")
            rule_list = [a for a in self.rules if a[0] == page]
            self.debug.print(3, f"rule list is currently {rule_list}")
            for [first, last] in rule_list:
                self.debug.print(3, f" checking rule {first}|{last}")
                if last in pages_dict:
                    if pages_dict[first] > pages_dict[last]:
                        rule_follower = False
                        break
        if rule_follower:
            self.debug.print(3, f"index {page_list} is a rule follower")
            middle_index = int((len(page_list) - 1) / 2)
            self.page_sum += int(page_list[middle_index])

    def solve(self):
        self.parse()
        self.print_run_info()
        if self.puzzle_part == "a":
            return self.page_sum
        else:
            return 0
