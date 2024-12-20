from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_items = len(isConnected)
        uf = UnionFind(n_items)

        for row_id in range(n_items):
            for col_id in range(row_id + 1, n_items):
                # upper triangle elements are enough!
                if isConnected[row_id][col_id] == 1:
                    uf.union(row_id, col_id)

        # counts can be internally tracked in the uf data structure
        return uf.get_count()

class UnionFind:
    def __init__(self, n_items):
        self.root = [i for i in range(n_items)]
        self.rank = [1] * n_items
        self.count = n_items

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            elif self.rank[root_y] < self.rank[root_x]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y
                
                
    def get_count(self,):
        return self.count


