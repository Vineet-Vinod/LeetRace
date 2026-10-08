class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return (max_row - min_row + 1) * (max_col - min_col + 1)
