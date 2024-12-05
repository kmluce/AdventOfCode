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
        self.rule_breakers = []
        self.left_set = set()
        self.right_set = set()

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
                        self.left_set.add(int(first))
                        self.right_set.add(int(last))
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
        else:
            self.rule_breakers.append(page_list)

    def fix_rule_breakers(self):
        left_rule_pages = []
        right_rule_pages = []
        for page in self.left_set:
            left_rule_pages[page] = set([x for x in self.rules[1] if self.rules[0] == page])
        for page in self.right_set:
            right_rule_pages[page] = set([x for x in self.rules[0] if self.rules[1] == page])
        for page_list in self.rule_breakers:
            self.debug.print(1, f"current rule breaker is {page_list}")
            tmp_page_list = []
            for current_page in page_list:
                self.debug.print(1, f"inserting page {current_page} into list {tmp_page_list}")
                if len(tmp_page_list) == 0:
                    tmp_page_list.append(current_page)
                else:
                    for split in range(len(tmp_page_list)):
                        self.debug.print(1, f"splitting at {split}")
                        if (set(tmp_page_list[0:split]).isdisjoint(left_rule_pages[current_page])
                            and set(tmp_page_list[split:-1]).isdisjoint(right_rule_pages[current_page])):
                            tmp_page_list.insert(split, current_page)
                self.debug.print(1, f"fully inserted list is {tmp_page_list}")

        return 0

    def solve(self):
        self.parse()
        self.print_run_info()
        if self.puzzle_part == "a":
            return self.page_sum
        else:
            return self.fix_rule_breakers()
