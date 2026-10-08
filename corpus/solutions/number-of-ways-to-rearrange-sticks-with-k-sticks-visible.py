class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for length in range(1, n + 1):
            for visible in range(min(length, k), 0, -1):
                dp[visible] = (dp[visible - 1] + (length - 1) * dp[visible]) % mod
            dp[0] = 0
        return dp[k]
