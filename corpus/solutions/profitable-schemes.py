class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for members in range(n, g - 1, -1):
                for earned in range(minProfit + 1):
                    value = min(minProfit, earned + p)
                    dp[members][value] = (
                        dp[members][value] + dp[members - g][earned]
                    ) % 1000000007
        return sum(row[minProfit] for row in dp) % 1000000007
