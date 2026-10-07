class Solution:
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        buses.sort()
        passengers.sort()
        i = 0
        last = []
        for bus in buses:
            count = 0
            while i < len(passengers) and passengers[i] <= bus and count < capacity:
                last.append(passengers[i])
                i += 1
                count += 1
            if bus == buses[-1]:
                boarded = count
        t = buses[-1] if boarded < capacity else last[-1] - 1
        occupied = set(passengers)
        while t in occupied:
            t -= 1
        return t
