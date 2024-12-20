from node import Node
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.tail.nxt_node = Node('dummy')
    
    def add(self, node):
        self.tail.nxt_node = node
        self.tail = node
        self.tail.nxt_node = Node('dummy')

class DoubleLinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.tail.nxt_node = Node('dummy')
    
    def add(self, node):
        if self.head is None:
            self.head= node
            self.tail= node
            self.tail.nxt_node = Node('dummy')
        else:
            old_tail = self.tail
            self.tail.nxt_node = node
            self.tail = node
            self.tail.prv_node = old_tail
            self.tail.nxt_node = Node('dummy')

    def pop(self):
        if self.head is None:
            raise ValueError('No elements to pop!')
        tail = self.tail
        if self.head == tail:
            self.head=None
            self.tail=None
        else:
            new_tail = tail.prv_node
            self.tail = new_tail
            self.tail.nxt_node = Node('dummy')
        return tail
