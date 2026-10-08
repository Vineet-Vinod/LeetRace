import heapq


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        fuel = startFuel
        available = []
        index = 0
        stops = 0
        while fuel < target:
            while index < len(stations) and stations[index][0] <= fuel:
                heapq.heappush(available, -stations[index][1])
                index += 1
            if not available:
                return -1
            fuel -= heapq.heappop(available)
            stops += 1
        return stops
