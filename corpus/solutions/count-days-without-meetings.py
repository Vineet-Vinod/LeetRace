class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_days = 0
        next_day = 1
        for start, end in meetings:
            if start > next_day:
                free_days += start - next_day
            next_day = max(next_day, end + 1)
        return free_days + max(0, days - next_day + 1)
