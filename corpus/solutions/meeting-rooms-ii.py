class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        active: list[int] = []
        maximum = 0
        for start, end in sorted(intervals):
            while active and active[0] <= start:
                heappop(active)
            heappush(active, end)
            maximum = max(maximum, len(active))
        return maximum
