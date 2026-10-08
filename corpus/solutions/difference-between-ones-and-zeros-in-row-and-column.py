class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        row_ones = [sum(row) for row in grid]
        col_ones = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]
        return [
            [2 * row_ones[r] - cols + 2 * col_ones[c] - rows for c in range(cols)]
            for r in range(rows)
        ]
