class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        a = [1] + [x for x in nums if x] + [1]
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                dp[left][right] = max(
                    dp[left][k] + dp[k][right] + a[left] * a[k] * a[right]
                    for k in range(left + 1, right)
                )
        return dp[0][-1]
