from collections import deque


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[m * n + 1] * n for _ in range(m)]
        distance[0][0] = 0
        queue = deque([(0, 0, 0)])
        while queue:
            d, i, j = queue.popleft()
            if d != distance[i][j]:
                continue
            if (i, j) == (m - 1, n - 1):
                return d
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    value = d + grid[x][y]
                    if value < distance[x][y]:
                        distance[x][y] = value
                        if grid[x][y]:
                            queue.append((value, x, y))
                        else:
                            queue.appendleft((value, x, y))
        return -1
