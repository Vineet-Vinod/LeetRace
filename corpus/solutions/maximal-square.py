class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        best = 0
        for r in range(1, rows + 1):
            diagonal = 0
            for c in range(1, cols + 1):
                previous = dp[c]
                if matrix[r - 1][c - 1] == "1":
                    dp[c] = 1 + min(dp[c], dp[c - 1], diagonal)
                    best = max(best, dp[c])
                else:
                    dp[c] = 0
                diagonal = previous
        return best * best
