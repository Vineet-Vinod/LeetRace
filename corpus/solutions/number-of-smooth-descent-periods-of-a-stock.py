class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        streak = 0
        total = 0
        previous = None
        for price in prices:
            streak = streak + 1 if previous is not None and previous - price == 1 else 1
            total += streak
            previous = price
        return total
