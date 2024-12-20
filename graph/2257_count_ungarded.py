from collections import deque
from typing import List


class Solution:
    def countUnguarded(self, row: int, column: int, guards: List[List[int]],
                       walls: List[List[int]]) -> int:
        grid = [[0] * column for _ in range(row)]
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'

        def expand(root_r, root_c):
            operation = [[-1, 0],  [1, 0], [0, 1], [0, -1]]
            for r_delta, c_delta in operation:
                r, c = root_r, root_c
                while True:
                    r, c = r + r_delta, c + c_delta
                    if not (r >= 0 and c >= 0 and r < row and c < column) \
                            or (grid[r][c] == 'G') or (grid[r][c] == 'W'):
                        break
                    grid[r][c] = -1
        queue = deque(guards)
        while queue:
            r, c = queue.popleft()
            expand(r, c)

        return sum([grid[r][c] == 0 for r in range(row)
                    for c in range(column)])
