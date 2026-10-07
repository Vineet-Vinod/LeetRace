from typing import List
from collections import Counter


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:  # noqa: E741 - names match the required candidate keyword interface.
        counts = Counter(nums)
        mod = 10**9 + 7
        r = min(r, sum(nums))
        if l > r:
            return 0
        dp = [0] * (r + 1)
        dp[0] = counts.pop(0, 0) + 1
        for value, count in counts.items():
            nxt = dp[:]
            for s in range(value, r + 1):
                nxt[s] += nxt[s - value]
                if s >= value * (count + 1):
                    nxt[s] -= dp[s - value * (count + 1)]
                nxt[s] %= mod
            dp = nxt
        return sum(dp[l : r + 1]) % mod
