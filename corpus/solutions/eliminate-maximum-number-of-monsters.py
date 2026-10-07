class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_minutes = sorted(
            (distance - 1) // velocity for distance, velocity in zip(dist, speed)
        )
        for minute, arrival in enumerate(arrival_minutes):
            if arrival < minute:
                return minute
        return len(dist)
