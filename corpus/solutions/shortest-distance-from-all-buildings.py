from typing import List
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        distances = [[0] * n for _ in grid]
        reached = [[0] * n for _ in grid]
        buildings = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                queue = deque([(r, c, 0)])
                found = 0
                while queue:
                    x, y, d = queue.popleft()
                    for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if (
                            0 <= a < m
                            and 0 <= b < n
                            and grid[a][b] == 0
                            and reached[a][b] == buildings
                        ):
                            reached[a][b] += 1
                            distances[a][b] += d + 1
                            found += 1
                            queue.append((a, b, d + 1))
                buildings += 1
                if not found:
                    return -1
        choices = [
            distances[r][c]
            for r in range(m)
            for c in range(n)
            if grid[r][c] == 0 and reached[r][c] == buildings
        ]
        return min(choices) if choices else -1
