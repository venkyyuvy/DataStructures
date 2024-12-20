"""
lc 543
"""

from typing import List, Optional

import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = [
    "diameterOfBinaryTree",
]

def test_clone_graph(solutions):
    for sol in solutions:
        arr = [1, 2, 3, 4, 5]
        root = construct_tree(arr)
        assert sol(root) == 3
        arr = [1, 2]
        root = construct_tree(arr)
        assert sol(root) == 1


# Definition for a Node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # Insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # Insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

def construct_tree(arr):
    n = len(arr)
    return insert_level_order(arr, None, 0, n)




class Solution:
    def diameterOfBinaryTree(self, root: Optional["Node"]) -> Optional["Node"]:
        max_dia = 0

        def dfs(curr_node):
            nonlocal max_dia
            if not curr_node:
                return 0
            left = dfs(curr_node.left)
            right = dfs(curr_node.right)
            max_dia = max(max_dia, left + right)
            return 1 + max(left, right)
        dfs(root)
        return max_dia
