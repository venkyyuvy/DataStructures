from itertools import islice
from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def traverse(node, queue):
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        return queue

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue, current = deque([root]), deque([])
        while queue:
            n = len(queue)
            current = self.traverse(queue[0], current)
            for i1, i2 in zip(range(n), range(1, n)):
                node1, node2 = queue[i1], queue[i2]
                node1.next = node2
                current = self.traverse(node2, current)

            queue, current = current, []
        return root

    def connect_leetcode(self, root: Optional['Node']) -> Optional['Node']:
        
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root
