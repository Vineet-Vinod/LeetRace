class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for end in range(1, len(arr) + 1):
            maximum = 0
            for length in range(1, min(k, end) + 1):
                maximum = max(maximum, arr[end - length])
                dp[end] = max(dp[end], dp[end - length] + maximum * length)
        return dp[-1]
