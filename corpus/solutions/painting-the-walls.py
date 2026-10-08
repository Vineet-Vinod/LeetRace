from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [10**20] * n
        for price, duration in zip(cost, time):
            for walls in range(n, 0, -1):
                dp[walls] = min(dp[walls], dp[max(0, walls - duration - 1)] + price)
        return dp[n]
