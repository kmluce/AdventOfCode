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
        self.rule_breakers_sum = 0

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
        left_rule_pages = {}
        right_rule_pages = {}
        print("rules are", self.rules)
        for page in self.left_set:
            left_rule_pages[page] = set([x[1] for x in self.rules if x[0] == page])
            print("left rule page for", page, "is", left_rule_pages[page])
        for page in self.right_set:
            right_rule_pages[page] = set([x[0] for x in self.rules if x[1] == page])
        for page_list in self.rule_breakers:
            self.debug.print(1, f"current rule breaker is {page_list}")
            tmp_page_list = []
            for current_page in page_list:
                self.debug.print(1, f"inserting page {current_page} into list {tmp_page_list}")
                if len(tmp_page_list) == 0:
                    tmp_page_list.append(current_page)
                else:
                    if current_page in left_rule_pages.keys():
                        if current_page in right_rule_pages.keys():
                            for split in range(len(tmp_page_list)+1):
                                self.debug.print(2, f"splitting at {split}")
                                self.debug.print(2,f"current list is {tmp_page_list}")
                                self.debug.print(2, f"testing to see if {tmp_page_list[0:split]} is disjoint from {left_rule_pages[current_page]}")
                                self.debug.print(2, f"testing to see if {tmp_page_list[split:]} is disjoint from {right_rule_pages[current_page]}")
                                if (set(tmp_page_list[0:split]).isdisjoint(left_rule_pages[current_page])
                                        and set(tmp_page_list[split:]).isdisjoint(right_rule_pages[current_page])):
                                    tmp_page_list.insert(split, current_page)
                                    break
                        else:
                            tmp_page_list.insert(0, current_page)
                    else:
                        tmp_page_list.append(current_page)
            self.debug.print(1, f"fully inserted list is {tmp_page_list}")
            middle_index = int((len(tmp_page_list) - 1) / 2)
            self.rule_breakers_sum += int(tmp_page_list[middle_index])
        return self.rule_breakers_sum


        return 0

    def solve(self):
        self.parse()
        self.print_run_info()
        if self.puzzle_part == "a":
            return self.page_sum
        else:
            return self.fix_rule_breakers()
