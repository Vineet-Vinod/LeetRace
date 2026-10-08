class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        remaining = 0
        furthest_end = -1
        for _, end in intervals:
            if end > furthest_end:
                remaining += 1
                furthest_end = end
        return remaining
