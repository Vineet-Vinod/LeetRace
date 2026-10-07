class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for cost, sale in zip(present, future):
            profit = sale - cost
            if profit <= 0 or cost > budget:
                continue
            for amount in range(budget, cost - 1, -1):
                dp[amount] = max(dp[amount], dp[amount - cost] + profit)
        return max(dp)
