class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for i, char in enumerate(s) if i == 0 or char != s[i - 1])
        n = len(s)
        dp = [[0] * n for _ in s]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                best = 1 + dp[i + 1][j]
                for t in range(i + 1, j + 1):
                    if s[t] == s[i]:
                        best = min(
                            best, (dp[i + 1][t - 1] if t > i + 1 else 0) + dp[t][j]
                        )
                dp[i][j] = best
        return dp[0][-1]
