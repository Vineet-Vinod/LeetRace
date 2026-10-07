class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        limit = round(hour * 100)

        def arrives(speed: int) -> bool:
            full_hours = sum((distance + speed - 1) // speed for distance in dist[:-1])
            return full_hours * 100 * speed + dist[-1] * 100 <= limit * speed

        low, high = 1, 10**7
        while low < high:
            middle = (low + high) // 2
            if arrives(middle):
                high = middle
            else:
                low = middle + 1
        return low if arrives(low) else -1
