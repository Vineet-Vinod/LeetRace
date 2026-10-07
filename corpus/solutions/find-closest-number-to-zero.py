class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return max(nums, key=lambda value: (-abs(value), value))
