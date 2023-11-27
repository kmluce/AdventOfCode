class Puzzle:

    def __init__(self, file_name: str):
        self.fileName = file_name
        self.rawNodeDefs = []
        self.messages = []
        self.highestPathNo = 0
        self.nodeTree = []

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                if len(line) == 0:
                    break
                self.rawNodeDefs.append(line)
                fields = line.split(":")
                if int(fields[0]) > self.highestPathNo:
                    self.highestPathNo = int(fields[0])

            for line in file:
                line = line.rstrip()
                self.messages.append(line)
        self.print_raw()
        self.nodeTree = (self.highestPathNo + 1) * [[None]]
        for line in self.rawNodeDefs:
            fields = line.split(":")
            curr_index: int = int(fields[0])
            self.nodeTree[curr_index] = fields[1].split("|")
            for x in range(len(self.nodeTree[curr_index])):
                self.nodeTree[curr_index][x] = self.nodeTree[curr_index][x].lstrip()
                self.nodeTree[curr_index][x] = self.nodeTree[curr_index][x].rstrip()
        self.print_cooked()

    def print_raw(self):
        print("Raw Node Map:", self.highestPathNo)
        for x in self.rawNodeDefs:
            print("   ", x)
        print("")
        print("Paths:")
        for x in self.messages:
            print("   ", x)

    def print_cooked(self):
        print("Cooked Node Map:", self.highestPathNo)
        for i in range(len(self.nodeTree)):
            print(i, ":", self.nodeTree[i])

    def node_partial_match(self, node: int, test_string: str) -> list:
        curr_letter_count=0
        print("testing", test_string, "against rule", node)
        print("  testing to see if the first character", self.nodeTree[node][0], "of", self.nodeTree[node],
              "is a quote")
        if not test_string:
            return []
        elif '"' in str(self.nodeTree[node][0]):
            match_string = self.nodeTree[node][0].replace('"', "")
            print("matching", match_string, "against", test_string)
            if test_string.startswith(match_string):
                print("matched, returning 1")
                return [len(match_string)]
        elif len(self.nodeTree[node]) == 1:
            node_list = [int(x) for x in self.nodeTree[node][0].split()]

            char_removal_list = [0]
            temp_char_removal_list = []
            temp_char_match_list = []
            for new_node in node_list:
                print("char removal list is", char_removal_list)
                for num_chars in char_removal_list:
                    print("rescursing with node", new_node, "and num removed chars", num_chars)
                    temp_char_match_list.extend(self.node_partial_match(new_node,test_string[num_chars:]))
                if not temp_char_match_list:
                    return []
                partial_num_char:int
                for partial_num_char in char_removal_list:
                    new_num_char:int
                    for new_num_char in temp_char_match_list:
                        temp_char_removal_list.append(int(partial_num_char) + int(new_num_char))
                char_removal_list = temp_char_removal_list
            return char_removal_list
        else:
            return[]

    def check_rules(self, rule, check_string):
        answer = self.node_partial_match(rule, check_string)
        if answer:
            return True
        else:
            return False


    def solvea(self):
        return None
