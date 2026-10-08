class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_counts = [sum(grid[row]) for row in range(rows)]
        col_counts = [sum(grid[row][col] for row in range(rows)) for col in range(cols)]
        return sum(
            grid[row][col] and (row_counts[row] > 1 or col_counts[col] > 1)
            for row in range(rows)
            for col in range(cols)
        )
