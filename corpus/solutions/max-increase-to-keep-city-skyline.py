class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(len(grid))) for c in range(len(grid))]
        return sum(
            min(row_max[r], col_max[c]) - grid[r][c]
            for r in range(len(grid))
            for c in range(len(grid))
        )
