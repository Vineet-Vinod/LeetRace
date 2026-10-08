class Solution:
    def maxScore(self, prices: List[int]) -> int:
        totals: dict[int, int] = {}
        for day, price in enumerate(prices, start=1):
            key = price - day
            totals[key] = totals.get(key, 0) + price
        return max(totals.values())
