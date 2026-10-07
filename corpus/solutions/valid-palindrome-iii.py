class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            diagonal = 0
            for j in range(i + 1, n):
                old = dp[j]
                dp[j] = diagonal if s[i] == s[j] else 1 + min(dp[j], dp[j - 1])
                diagonal = old
        return dp[-1] <= k
