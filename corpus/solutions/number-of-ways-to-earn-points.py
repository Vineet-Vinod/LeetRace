class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * target
        for count, mark in types:
            nxt = [0] * (target + 1)
            for residue in range(min(mark, target + 1)):
                window = 0
                for total in range(residue, target + 1, mark):
                    window += dp[total]
                    if total - (count + 1) * mark >= 0:
                        window -= dp[total - (count + 1) * mark]
                    nxt[total] = window % mod
            dp = nxt
        return dp[target]
