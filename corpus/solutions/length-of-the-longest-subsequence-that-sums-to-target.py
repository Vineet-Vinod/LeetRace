class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-(10**9)] * (target + 1)
        dp[0] = 0
        for value in nums:
            for total in range(target, value - 1, -1):
                dp[total] = max(dp[total], dp[total - value] + 1)
        return dp[target] if dp[target] >= 0 else -1
