class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minimum = [[10**18] * cols for _ in range(rows)]
        best = -(10**18)
        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    best = max(best, grid[r][c] - minimum[r - 1][c])
                    minimum[r][c] = min(minimum[r][c], minimum[r - 1][c])
                if c > 0:
                    best = max(best, grid[r][c] - minimum[r][c - 1])
                    minimum[r][c] = min(minimum[r][c], minimum[r][c - 1])
                minimum[r][c] = min(minimum[r][c], grid[r][c])
        return best
