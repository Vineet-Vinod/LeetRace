class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        low = nums.index(min(nums))
        high = nums.index(max(nums))
        first, last = sorted((low, high))
        return min(last + 1, len(nums) - first, first + 1 + len(nums) - last)
