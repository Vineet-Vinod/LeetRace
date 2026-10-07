from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[0] * k for _ in grid[0]]
        dp[0][0] = 1
        for row in grid:
            left = [0] * k
            for j, value in enumerate(row):
                new = [0] * k
                for r in range(k):
                    new[(r + value) % k] = (dp[j][r] + left[r]) % 1000000007
                dp[j] = left = new
        return dp[-1][0]
