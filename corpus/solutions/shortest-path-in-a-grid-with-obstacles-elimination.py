from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        best = [[-1] * n for _ in range(m)]
        best[0][0] = k
        queue = deque([(0, 0, k, 0)])
        while queue:
            r, c, remaining, distance = queue.popleft()
            if (r, c) == (m - 1, n - 1):
                return distance
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    after = remaining - grid[nr][nc]
                    if after >= 0 and after > best[nr][nc]:
                        best[nr][nc] = after
                        queue.append((nr, nc, after, distance + 1))
        return -1
