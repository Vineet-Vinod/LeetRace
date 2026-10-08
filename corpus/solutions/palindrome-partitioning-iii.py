class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        costs = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                costs[i][j] = (s[i] != s[j]) + (
                    costs[i + 1][j - 1] if length > 2 else 0
                )
        dp = [0] + [n] * n
        for parts in range(1, k + 1):
            new = [n] * (n + 1)
            for end in range(parts, n + 1):
                new[end] = min(
                    dp[start] + costs[start][end - 1] for start in range(parts - 1, end)
                )
            dp = new
        return dp[n]
