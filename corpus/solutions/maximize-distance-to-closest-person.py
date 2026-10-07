class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = [index for index, seat in enumerate(seats) if seat]
        best = max(occupied[0], len(seats) - 1 - occupied[-1])
        for left, right in zip(occupied, occupied[1:]):
            best = max(best, (right - left) // 2)
        return best
