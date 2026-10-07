class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        import math

        gaps = [b - a for a, b in zip(stations, stations[1:])]
        lo, hi = 0.0, float(max(gaps))
        for _ in range(65):
            mid = (lo + hi) / 2
            needed = sum(math.ceil(gap / mid) - 1 for gap in gaps)
            if needed <= k:
                hi = mid
            else:
                lo = mid
        return hi
