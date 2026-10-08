class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minimum = min(nums)
        if any(value % minimum for value in nums):
            return 1
        return max(1, (nums.count(minimum) + 1) // 2)
