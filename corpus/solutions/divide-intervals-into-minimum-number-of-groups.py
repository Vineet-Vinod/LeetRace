class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        active: List[int] = []
        maximum = 0
        for left, right in sorted(intervals):
            while active and active[0] < left:
                heappop(active)
            heappush(active, right)
            maximum = max(maximum, len(active))
        return maximum
