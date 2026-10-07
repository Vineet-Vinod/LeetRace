from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        columns = [[] for _ in range(n)]
        result = -1
        for i, row in enumerate(grid):
            active = []
            for j, value in enumerate(row):
                while active and active[0][1] < j:
                    heappop(active)
                while columns[j] and columns[j][0][1] < i:
                    heappop(columns[j])
                distance = (
                    1
                    if i == 0 and j == 0
                    else min(
                        active[0][0] if active else 10**9,
                        columns[j][0][0] if columns[j] else 10**9,
                    )
                )
                if distance < 10**9:
                    heappush(active, (distance + 1, j + value))
                    heappush(columns[j], (distance + 1, i + value))
                if i == m - 1 and j == n - 1:
                    result = distance if distance < 10**9 else -1
        return result
