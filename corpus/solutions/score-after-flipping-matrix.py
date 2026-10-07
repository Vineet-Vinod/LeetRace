class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        for c in range(n):
            ones = sum(row[c] == row[0] for row in grid)
            total += max(ones, m - ones) * (1 << (n - c - 1))
        return total
