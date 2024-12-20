from typing import List
from unionfind import UnionFind

class Edge:
    def __init__(self, start, end, weight) -> None:
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other) -> bool:
        return self.weight < other.weight

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        for row_id, start in enumerate(points):
            for col_id, end in enumerate(points[row_id + 1:], start = row_id+1): 
                weight = abs(start[0]-end[0]) + abs(start[1]-end[1])
                edges.append(Edge(row_id, col_id, weight))

        edges.sort()
        remaining_edges = len(points) - 1 
        cost = 0
        uf = UnionFind(len(points))

        for edge in edges:
            if not uf.connected(edge.start, edge.end):
                uf.union(edge.start, edge.end)
                cost += edge.weight
                remaining_edges -= 1
                if remaining_edges == 0:
                    break
        return cost