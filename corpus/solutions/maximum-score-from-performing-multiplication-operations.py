from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        dp = [0] * (m + 1)
        for operation in range(m - 1, -1, -1):
            following = dp[:]
            for left in range(operation + 1):
                right = n - 1 - (operation - left)
                following[left] = max(
                    multipliers[operation] * nums[left] + dp[left + 1],
                    multipliers[operation] * nums[right] + dp[left],
                )
            dp = following
        return dp[0]
