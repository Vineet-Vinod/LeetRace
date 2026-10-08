class Solution:
    def minOperationsMaxProfit(
        self, customers: list[int], boardingCost: int, runningCost: int
    ) -> int:
        waiting = boarded = rotations = best_profit = 0
        best_rotation = -1
        while rotations < len(customers) or waiting:
            if rotations < len(customers):
                waiting += customers[rotations]
            take = min(4, waiting)
            waiting -= take
            boarded += take
            rotations += 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > best_profit:
                best_profit = profit
                best_rotation = rotations
        return best_rotation
