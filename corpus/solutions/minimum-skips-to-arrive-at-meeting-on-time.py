from __future__ import annotations
from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1
        n = len(dist)
        inf = 10**30
        dp = [0] + [inf] * n
        for i, length in enumerate(dist):
            next_dp = [inf] * (n + 1)
            for skips in range(i + 1):
                finish = dp[skips] + length
                rounded = (
                    finish if i == n - 1 else (finish + speed - 1) // speed * speed
                )
                next_dp[skips] = min(next_dp[skips], rounded)
                if i < n - 1:
                    next_dp[skips + 1] = min(next_dp[skips + 1], finish)
            dp = next_dp
        return next(i for i, time in enumerate(dp) if time <= speed * hoursBefore)
