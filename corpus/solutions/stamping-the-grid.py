from typing import List


class Solution:
    def possibleToStamp(
        self, grid: List[List[int]], stampHeight: int, stampWidth: int
    ) -> bool:
        rows, cols = len(grid), len(grid[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    grid[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )
        coverage = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - stampHeight + 1):
            for c in range(cols - stampWidth + 1):
                bottom, right = r + stampHeight, c + stampWidth
                occupied = (
                    prefix[bottom][right]
                    - prefix[r][right]
                    - prefix[bottom][c]
                    + prefix[r][c]
                )
                if occupied == 0:
                    coverage[r][c] += 1
                    coverage[bottom][c] -= 1
                    coverage[r][right] -= 1
                    coverage[bottom][right] += 1
        for r in range(rows):
            for c in range(cols):
                if r:
                    coverage[r][c] += coverage[r - 1][c]
                if c:
                    coverage[r][c] += coverage[r][c - 1]
                if r and c:
                    coverage[r][c] -= coverage[r - 1][c - 1]
                if not grid[r][c] and coverage[r][c] == 0:
                    return False
        return True
