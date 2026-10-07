from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)
        queue = deque([(0, 0, 0, 0)])
        seen = {(0, 0, 0)}
        while queue:
            r, c, vertical, distance = queue.popleft()
            if (r, c, vertical) == (n - 1, n - 2, 0):
                return distance
            moves = []
            if vertical == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    moves.append((r, c + 1, 0))
                if r + 1 < n and grid[r + 1][c] == grid[r + 1][c + 1] == 0:
                    moves.extend(((r + 1, c, 0), (r, c, 1)))
            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    moves.append((r + 1, c, 1))
                if c + 1 < n and grid[r][c + 1] == grid[r + 1][c + 1] == 0:
                    moves.extend(((r, c + 1, 1), (r, c, 0)))
            for state in moves:
                if state not in seen:
                    seen.add(state)
                    queue.append((*state, distance + 1))
        return -1
