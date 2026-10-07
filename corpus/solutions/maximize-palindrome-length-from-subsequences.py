class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [0] * n
        answer = 0
        for i in range(n - 1, -1, -1):
            inner = 0
            dp[i] = 1
            for j in range(i + 1, n):
                old = dp[j]
                if s[i] == s[j]:
                    dp[j] = inner + 2
                    if i < len(word1) <= j:
                        answer = max(answer, dp[j])
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                inner = old
        return answer
