class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        width = min(arrLen, steps // 2 + 1)
        dp = [1] + [0] * (width - 1)
        for _ in range(steps):
            dp = [
                (dp[i] + (dp[i - 1] if i else 0) + (dp[i + 1] if i + 1 < width else 0))
                % (10**9 + 7)
                for i in range(width)
            ]
        return dp[0]
