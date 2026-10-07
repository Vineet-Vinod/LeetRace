class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        start, end = newInterval
        index = 0
        while index < len(intervals) and intervals[index][1] < start:
            result.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][0] <= end:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1
        result.append([start, end])
        result.extend(intervals[index:])
        return result
