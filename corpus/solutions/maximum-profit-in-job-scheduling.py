from typing import List
from bisect import bisect_right


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [job[0] for job in jobs]
        dp = [0]
        for i, (end, start, value) in enumerate(jobs):
            previous = bisect_right(ends, start, 0, i)
            dp.append(max(dp[-1], dp[previous] + value))
        return dp[-1]
