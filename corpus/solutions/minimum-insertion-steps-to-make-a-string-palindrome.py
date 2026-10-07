class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s) - 2, -1, -1):
            diagonal = 0
            for j in range(i + 1, len(s)):
                old = dp[j]
                dp[j] = diagonal if s[i] == s[j] else 1 + min(dp[j], dp[j - 1])
                diagonal = old
        return dp[-1]
