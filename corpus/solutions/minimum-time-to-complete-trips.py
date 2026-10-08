class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, min(time) * totalTrips
        while low < high:
            middle = (low + high) // 2
            if sum(middle // duration for duration in time) >= totalTrips:
                high = middle
            else:
                low = middle + 1
        return low
