"""
lc 133
"""

from typing import List, Optional

import pytest

pytest.problem_name = __name__.split(".")[-1]
pytest.method_names = [
    "cloneGraph",
]

def test_clone_graph(solutions):
    for sol in solutions:
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        assert sol(createGraph(adj_list)) is not None
        assert create_adj_list_from_graph(
            sol(createGraph(adj_list))) == adj_list
        assert sol(createGraph([])) is None


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def createGraph(adjList):
    if not adjList:
        return None
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def create_adj_list_from_graph(root):
    if root is None:
        return []
    adj = {}
    seen = set()
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)
        adj[node.val] = [neighbor.val for neighbor in node.neighbors]
        queue.extend(node.neighbors)
    adj_list = [adj[node + 1] for node in range(len(adj))]
    return adj_list


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        old_to_new = {}

        def dfs(node):
            if new_node := old_to_new.get(node):
                return new_node

            new_node = Node(node.val)
            old_to_new[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node

        return dfs(node) if node else None
