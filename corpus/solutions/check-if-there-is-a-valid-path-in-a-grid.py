from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        openings = {
            1: {(0, -1), (0, 1)},
            2: {(-1, 0), (1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(0, 1), (1, 0)},
            5: {(0, -1), (-1, 0)},
            6: {(0, 1), (-1, 0)},
        }
        queue = deque([(0, 0)])
        seen = {(0, 0)}
        while queue:
            row, col = queue.popleft()
            if (row, col) == (rows - 1, cols - 1):
                return True
            for dr, dc in openings[grid[row][col]]:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in seen:
                    continue
                if (-dr, -dc) in openings[grid[nr][nc]]:
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return False
