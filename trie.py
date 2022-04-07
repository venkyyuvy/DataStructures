
class Node:
    def __init__(self, n_chars=26):
        self.chars = [None] * n_chars
        self.count = 0

    def get_node(self, char) -> Node:
        return self.chars[ord('a') - ord(char)]

    def set_node(self, char, node: Node) -> None:
        self.chars[ord('a') - ord(char)] = node

    def add(self, string: str, index: int) -> None:
        self.count += 1
        if index == len(string):
            return
        char = string[index]
        if node := self.get_node(char):
            node.add(string, index + 1)
        else:
            node = Node()
            self.set_node(char, )
            node.add(string, index + 1)

    def findCount(self, string: str, index: int) -> int:
        if index == len(string):
            return self.count

        if node := self.get_node(string[index]):
            return node.findCount(string, index + 1)
        return 0



