class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            previous = 0
            for j, char2 in enumerate(text2, 1):
                old = dp[j]
                if char1 == char2:
                    dp[j] = previous + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                previous = old
        return dp[-1]
