class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = list(range(-1, n))
        for center in range(n):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < n and s[left] == s[right]:
                    dp[right + 1] = min(dp[right + 1], dp[left] + 1)
                    left -= 1
                    right += 1
        return dp[n]
