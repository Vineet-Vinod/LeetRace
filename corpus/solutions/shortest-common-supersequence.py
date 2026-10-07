class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = 1 + (
                    dp[i + 1][j + 1]
                    if str1[i] == str2[j]
                    else min(dp[i + 1][j], dp[i][j + 1])
                )
        i = j = 0
        out = []
        while i < m and j < n:
            if str1[i] == str2[j]:
                out.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] < dp[i][j + 1] or (
                dp[i + 1][j] == dp[i][j + 1] and str1[i] < str2[j]
            ):
                out.append(str1[i])
                i += 1
            else:
                out.append(str2[j])
                j += 1
        return "".join(out) + str1[i:] + str2[j:]
