class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, bisect_right(nums, target) - 1]
