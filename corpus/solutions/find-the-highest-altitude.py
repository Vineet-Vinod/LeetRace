class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = best = 0
        for change in gain:
            altitude += change
            best = max(best, altitude)
        return best
