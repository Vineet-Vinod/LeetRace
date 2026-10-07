class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [1] * (n + 1)
        lcp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            row = [0] * (n + 1)
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    row[j] = lcp[j + 1] + 1
                    size = j - i
                    if row[j] >= size:
                        dp[i] = max(dp[i], 1 + dp[j])
            lcp = row
        return dp[0]
