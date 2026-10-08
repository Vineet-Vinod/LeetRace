from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        distance = [[rows * cols + 1] * cols for _ in grid]
        distance[0][0] = 0
        queue = deque([(0, 0)])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            r, c = queue.popleft()
            for sign, (dr, dc) in enumerate(directions, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    weight = int(grid[r][c] != sign)
                    if distance[r][c] + weight < distance[nr][nc]:
                        distance[nr][nc] = distance[r][c] + weight
                        if weight:
                            queue.append((nr, nc))
                        else:
                            queue.appendleft((nr, nc))
        return distance[-1][-1]
