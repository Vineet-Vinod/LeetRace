class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = defaultdict(int)
        for passengers, start, end in trips:
            events[start] += passengers
            events[end] -= passengers
        load = 0
        for location in sorted(events):
            load += events[location]
            if load > capacity:
                return False
        return True
