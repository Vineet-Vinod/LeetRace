class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_flips = 0
        for r in range(rows):
            for c in range(cols // 2):
                row_flips += grid[r][c] != grid[r][cols - 1 - c]
        column_flips = 0
        for r in range(rows // 2):
            for c in range(cols):
                column_flips += grid[r][c] != grid[rows - 1 - r][c]
        return min(row_flips, column_flips)
