class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = best = nums[0]
        for i in range(1, len(nums)):
            current = current + nums[i] if nums[i] > nums[i - 1] else nums[i]
            best = max(best, current)
        return best
