class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for left in range(n - 1, -1, -1):
            diagonal = 0
            for right in range(left + 1, n):
                previous = dp[right]
                if s[left] == s[right]:
                    dp[right] = diagonal + 2
                else:
                    dp[right] = max(dp[right], dp[right - 1])
                diagonal = previous
        return dp[-1]
