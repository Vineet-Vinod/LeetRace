class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = decreasing = best = 1
        for previous, current in zip(nums, nums[1:]):
            increasing = increasing + 1 if current > previous else 1
            decreasing = decreasing + 1 if current < previous else 1
            best = max(best, increasing, decreasing)
        return best
