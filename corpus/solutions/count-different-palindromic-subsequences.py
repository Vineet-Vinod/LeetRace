class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        previous = [-1] * n
        following = [n] * n
        last = {}
        for i, ch in enumerate(s):
            previous[i] = last.get(ch, -1)
            last[ch] = i
        last = {}
        for i in range(n - 1, -1, -1):
            following[i] = last.get(s[i], n)
            last[s[i]] = i
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                middle = dp[i + 1][j - 1] if j > i + 1 else 0
                if s[i] != s[j]:
                    value = dp[i + 1][j] + dp[i][j - 1] - middle
                else:
                    lo, hi = following[i], previous[j]
                    if lo > hi:
                        value = 2 * middle + 2
                    elif lo == hi:
                        value = 2 * middle + 1
                    else:
                        value = 2 * middle - (dp[lo + 1][hi - 1] if hi > lo + 1 else 0)
                dp[i][j] = value % 1_000_000_007
        return dp[0][-1]
