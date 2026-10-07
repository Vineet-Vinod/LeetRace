from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        requirements_map = dict(requirements)
        limit = requirements_map[n - 1]
        dp = [1] + [0] * limit
        mod = 10**9 + 7
        for end in range(n):
            window = 0
            nxt = [0] * (limit + 1)
            for inv in range(limit + 1):
                window += dp[inv]
                if inv > end:
                    window -= dp[inv - end - 1]
                nxt[inv] = window % mod
            if end in requirements_map:
                needed = requirements_map[end]
                if needed > limit:
                    return 0
                nxt = [v if j == needed else 0 for j, v in enumerate(nxt)]
            dp = nxt
        return dp[limit]
