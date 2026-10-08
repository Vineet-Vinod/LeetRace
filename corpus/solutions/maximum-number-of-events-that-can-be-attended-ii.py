from typing import List
from bisect import bisect_right


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events)
        starts = [e[0] for e in events]
        n = len(events)
        nexts = [bisect_right(starts, e[1]) for e in events]
        dp = [0] * (n + 1)
        for _ in range(k):
            nxt = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                nxt[i] = max(nxt[i + 1], events[i][2] + dp[nexts[i]])
            dp = nxt
        return dp[0]
