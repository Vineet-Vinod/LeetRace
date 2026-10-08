from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        a = sorted(houses)
        n = len(a)
        cost = [[0] * n for _ in a]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = (cost[i + 1][j - 1] if length > 2 else 0) + a[j] - a[i]
        dp = [0] + [10**20] * n
        for _ in range(k):
            dp = [0] + [
                min(dp[j] + cost[j][i - 1] for j in range(i)) for i in range(1, n + 1)
            ]
        return dp[n]
