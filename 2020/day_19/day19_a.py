import fileinput
from typing import List


class NumberedGraphNode:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.childNodeSets = []
        self.hasMatchVal = False
        self.matchVal = ""

    def set_match_val(self, val):
        self.matchVal = str(val)
        self.hasMatchVal = True

    def add_path_set(self, val:str ):
        val = val.strip()
        self.childNodeSets.append(val)

    def get_node_id(self) -> int:
        return self.node_id

    def get_has_match_val(self) -> bool:
        return self.hasMatchVal

    def get_paths(self):
        return self.childNodeSets


class MessageGraph:
    def __init__(self, root_node_id: int, root_node_val) -> None:
        self.node_list: List[NumberedGraphNode] = [None] * 1
        self.root_node : NumberedGraphNode = NumberedGraphNode(root_node_id)
        self.node_list[root_node_id] = (self.root_node)
        # nodeSet = {int(root_node_id) : root_node}
        self.set_node_val(root_node_id, root_node_val)

    def set_node_val(self, node_id, node_val):
        print("setting node ID", node_id, "to", node_val)
        if "\"" in node_val:
            self.set_node_match(node_id, node_val)
        else:
            self.set_node_paths(node_id, node_val)

    def set_node_paths(self, node_id, node_val):
        for path_set in node_val.split('|'):
            path_set = path_set.strip()
            print("  Adding path set", path_set, "to node ID", node_id)
            path_array = [self.find_or_create_node(int(i)) for i in path_set.split(" ")]
            print("  Adding path array to node ID", node_id)
            for i in path_array:
                print(i.get_node_id())
            self.node_list[node_id].add_path_set(path_set)

    def set_node_match(self, node_id, node_val):
        node_val = node_val.strip("\"")
        print("   setting match to", node_val)
        self.node_list[node_id].set_match_val(node_val)

    def find_or_create_node(self, node_id: int):
        if node_id >= len(self.node_list):
            print("  list is", len(self.node_list), "nodes long")
            print("  appending", node_id - len(self.node_list) + 1, "nodes to list")
            for i in range(len(self.node_list) - 1, node_id):
                self.node_list.append(None)
        if self.node_list[node_id] is None:
            self.node_list[node_id] = NumberedGraphNode(node_id)
        return self.node_list[node_id]

    def check_message_against_graph(self, message: str, node_ids: str):
        print("  Checking message", message, "against paths", node_ids)
        return_val = True
        for next_node in node_ids.split(" "):
            print("  checking node against path", next_node)
            check_node = self.node_list[next_node]
            if check_node.get_has_match_val:
                print("  found bottom of list at node", next_node)
            else:
                new
                if next_node.get_paths():
                    pass



if __name__ == '__main__':
    nodeDefPhase = True
    myMessageGraph = 0
    for line in fileinput.input():
        line = line.rstrip()
        if fileinput.isfirstline():
            print("adding root node:", line)
            myRootNodeID, myRootPaths = line.split(':')
            myRootPaths = myRootPaths.strip()
            myMessageGraph = MessageGraph(int(myRootNodeID), myRootPaths)

        elif len(line.strip()) == 0:
            nodeDefPhase = False
        elif nodeDefPhase:
            print("adding node:", line)
            my_node_id, my_val = line.split(':')
            my_val = my_val.strip()
            my_node_id = int(my_node_id)
            myMessageGraph.find_or_create_node(my_node_id)
            myMessageGraph.set_node_val(my_node_id, my_val)
        else:
            print("checking pattern", line, ":")
            myMessageGraph.check_message_against_graph(line, "0")
