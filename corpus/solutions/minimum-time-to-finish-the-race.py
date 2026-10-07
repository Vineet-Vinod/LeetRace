from typing import List


class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        best_first = min(f for f, r in tires)
        best = [10**30] * (numLaps + 1)
        longest = 0
        for f, r in tires:
            lap, total, length = f, 0, 0
            while length < numLaps and lap <= changeTime + best_first:
                total += lap
                length += 1
                best[length] = min(best[length], total)
                lap *= r
            longest = max(longest, length)
        dp = [-changeTime] + [10**30] * numLaps
        for laps in range(1, numLaps + 1):
            dp[laps] = min(
                dp[laps - run] + changeTime + best[run]
                for run in range(1, min(laps, longest) + 1)
            )
        return dp[-1]
