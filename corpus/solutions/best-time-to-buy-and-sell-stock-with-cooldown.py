class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0
        for price in prices[1:]:
            previous_hold, previous_sold, previous_rest = hold, sold, rest
            hold = max(previous_hold, previous_rest - price)
            sold = previous_hold + price
            rest = max(previous_rest, previous_sold)
        return max(sold, rest)
