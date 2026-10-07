class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [sum(grid[r][0] != digit for r in range(rows)) for digit in range(10)]
        for c in range(1, cols):
            costs = [
                sum(grid[r][c] != digit for r in range(rows)) for digit in range(10)
            ]
            dp = [
                costs[digit] + min(dp[other] for other in range(10) if other != digit)
                for digit in range(10)
            ]
        return min(dp)
