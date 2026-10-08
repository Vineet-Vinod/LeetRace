class Solution:
    def houseOfCards(self, n: int) -> int:
        # A row with t triangles uses 3t-1 cards; each additional row needs at least one support card per triangle.
        dp = [0] * (n + 1)
        dp[0] = 1
        row = 1
        while 3 * row - 1 <= n:
            cost = 3 * row - 1
            for total in range(n, cost - 1, -1):
                dp[total] += dp[total - cost]
            row += 1
        return dp[n]
