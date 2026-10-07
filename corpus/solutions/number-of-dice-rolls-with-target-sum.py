class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            next_dp = [0] * (target + 1)
            for total, ways in enumerate(dp):
                if ways:
                    for face in range(1, min(k, target - total) + 1):
                        next_dp[total + face] = (next_dp[total + face] + ways) % mod
            dp = next_dp
        return dp[target]
