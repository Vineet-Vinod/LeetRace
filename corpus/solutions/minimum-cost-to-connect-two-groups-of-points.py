from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        len(cost)
        n = len(cost[0])
        size = 1 << n
        dp = [10**9] * size
        dp[0] = 0
        for row in cost:
            nxt = [10**9] * size
            for mask, value in enumerate(dp):
                if value == 10**9:
                    continue
                for j, c in enumerate(row):
                    target = mask | 1 << j
                    nxt[target] = min(nxt[target], value + c)
            dp = nxt
        cheapest = [min(row[j] for row in cost) for j in range(n)]
        return min(
            value + sum(cheapest[j] for j in range(n) if not mask >> j & 1)
            for mask, value in enumerate(dp)
        )
