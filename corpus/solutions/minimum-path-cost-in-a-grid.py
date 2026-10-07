class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = grid[0][:]
        for r in range(1, rows):
            next_dp = [10**18] * cols
            for c in range(cols):
                for next_col in range(cols):
                    next_dp[next_col] = min(
                        next_dp[next_col],
                        dp[c] + moveCost[grid[r - 1][c]][next_col] + grid[r][next_col],
                    )
            dp = next_dp
        return min(dp)
