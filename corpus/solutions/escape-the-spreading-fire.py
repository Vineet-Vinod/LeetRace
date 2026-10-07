from collections import deque
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        infinity = 10**9 + m * n + 1
        fire = [[infinity] * n for _ in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire[r][c] = 0
                    queue.append((r, c))
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] != 2
                    and fire[nr][nc] == infinity
                ):
                    fire[nr][nc] = fire[r][c] + 1
                    queue.append((nr, nc))

        def possible(wait: int) -> bool:
            if wait >= fire[0][0]:
                return False
            queue = deque([(0, 0, wait)])
            seen = {(0, 0)}
            while queue:
                r, c, time = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        not (0 <= nr < m and 0 <= nc < n)
                        or grid[nr][nc] != 0
                        or (nr, nc) in seen
                    ):
                        continue
                    arrival = time + 1
                    if (nr, nc) == (m - 1, n - 1):
                        if arrival <= fire[nr][nc]:
                            return True
                    elif arrival < fire[nr][nc]:
                        seen.add((nr, nc))
                        queue.append((nr, nc, arrival))
            return False

        if not possible(0):
            return -1
        if possible(10**9):
            return 10**9
        low, high = 0, m * n
        while low < high:
            middle = (low + high + 1) // 2
            if possible(middle):
                low = middle
            else:
                high = middle - 1
        return low
