class Solution:
    def minCostSetTime(
        self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int
    ) -> int:
        best = float("inf")
        for minutes in range(100):
            seconds = targetSeconds - 60 * minutes
            if 0 <= seconds <= 99:
                digits = f"{minutes:02d}{seconds:02d}".lstrip("0") or "0"
                finger = startAt
                cost = 0
                for char in digits:
                    digit = int(char)
                    if digit != finger:
                        cost += moveCost
                    cost += pushCost
                    finger = digit
                best = min(best, cost)
        return int(best)
