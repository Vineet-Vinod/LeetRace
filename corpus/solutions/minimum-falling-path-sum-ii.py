from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0][:]
        for row in grid[1:]:
            first, second = sorted(range(len(dp)), key=dp.__getitem__)[:2]
            dp = [
                value + dp[second if j == first else first]
                for j, value in enumerate(row)
            ]
        return min(dp)
