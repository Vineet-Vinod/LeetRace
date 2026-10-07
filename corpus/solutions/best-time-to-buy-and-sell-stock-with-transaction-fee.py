class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        holding = -prices[0]
        for price in prices[1:]:
            previous_cash = cash
            cash = max(cash, holding + price - fee)
            holding = max(holding, previous_cash - price)
        return cash
