class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [10**30] * n
        for end in range(1, n + 1):
            counts = [0] * n
            trimmed = 0
            for start in range(end - 1, -1, -1):
                value = nums[start]
                counts[value] += 1
                if counts[value] == 2:
                    trimmed += 2
                elif counts[value] > 2:
                    trimmed += 1
                dp[end] = min(dp[end], dp[start] + k + trimmed)
        return dp[n]
