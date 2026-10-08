class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_arrival = 0.0
        for start, velocity in cars:
            arrival = (target - start) / velocity
            if arrival > slowest_arrival:
                fleets += 1
                slowest_arrival = arrival
        return fleets
