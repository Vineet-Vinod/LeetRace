class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in arr]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                best = 1 + dp[i + 1][j]
                if arr[i] == arr[i + 1]:
                    best = min(best, 1 + (dp[i + 2][j] if i + 2 <= j else 0))
                for t in range(i + 2, j + 1):
                    if arr[t] == arr[i]:
                        best = min(
                            best, dp[i + 1][t - 1] + (dp[t + 1][j] if t < j else 0)
                        )
                dp[i][j] = best
        return dp[0][-1]
