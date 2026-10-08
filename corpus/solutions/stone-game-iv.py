from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = [i * i for i in range(1, isqrt(n) + 1)]
        for x in range(1, n + 1):
            for square in squares:
                if square > x:
                    break
                if not dp[x - square]:
                    dp[x] = True
                    break
        return dp[n]
