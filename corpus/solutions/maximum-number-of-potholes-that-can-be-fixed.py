class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        runs = sorted((len(part) for part in road.split(".") if part), reverse=True)
        fixed = 0
        for length in runs:
            if budget <= 1:
                break
            amount = min(length, budget - 1)
            fixed += amount
            budget -= amount + 1
        return fixed
