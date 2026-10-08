class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        ordered = sorted(intervals)
        return all(
            ordered[index - 1][1] <= ordered[index][0]
            for index in range(1, len(ordered))
        )
