class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            speed = (low + high) // 2
            hours = sum((pile + speed - 1) // speed for pile in piles)
            if hours <= h:
                high = speed
            else:
                low = speed + 1
        return low
