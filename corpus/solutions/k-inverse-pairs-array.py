class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k > n * (n - 1) // 2:
            return 0
        dp = [1] + [0] * k
        for size in range(1, n + 1):
            next_dp = [0] * (k + 1)
            window = 0
            for j in range(k + 1):
                window += dp[j]
                if j >= size:
                    window -= dp[j - size]
                window %= 1000000007
                next_dp[j] = window
            dp = next_dp
        return dp[k]
