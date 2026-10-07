class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap: list[int] = []
        index = 0
        day = 0
        attended = 0
        while index < len(events) or heap:
            if not heap:
                day = max(day, events[index][0])
            while index < len(events) and events[index][0] <= day:
                heappush(heap, events[index][1])
                index += 1
            while heap and heap[0] < day:
                heappop(heap)
            if heap:
                heappop(heap)
                attended += 1
                day += 1
        return attended
