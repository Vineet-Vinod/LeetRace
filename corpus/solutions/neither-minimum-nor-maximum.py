class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        low, high = min(nums), max(nums)
        return min(value for value in nums if low < value < high)
