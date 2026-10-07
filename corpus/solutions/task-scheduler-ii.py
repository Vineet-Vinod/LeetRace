class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_day = 1
        last_day = {}
        for task in tasks:
            if task in last_day:
                next_day = max(next_day, last_day[task] + space + 1)
            last_day[task] = next_day
            next_day += 1
        return next_day - 1
