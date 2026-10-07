class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for price in prices[1:]:
            best = max(best, price - lowest)
            lowest = min(lowest, price)
        return best
