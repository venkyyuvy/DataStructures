"""
least recently used cache (LRU cache)
LRUCache(10)

add(2)
add(3)
add(4)
get(4)
get(4)
get(4)
"""

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.hash = {}
        self.ll = DoubleLinkedList()

    def add(self, key, value) -> None:
        if len(self.hash) > self.capacity:
            head_node = self.ll.head
            self.ll.head = head_node.right
            del hash[head_node.key]

        node = Node(key, value)
        if not self.ll.head:
            self.ll.head = node
            self.ll.tail = node
        else:
            self.ll.head.left = node
            node.right = self.ll.head
            self.ll.head = node
        
        self.hash[key] = node.value

    def get(self, key) -> str:
        node = self.hash[key]
        if node.left: node.right.left = node.left
        if node.right: node.left.right = node.right
        self.ll.tail.right = node
        node.left = self.ll.tail
        self.ll.tail = node



