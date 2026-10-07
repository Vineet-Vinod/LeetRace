class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        first = nums.index(1)
        last = nums.index(len(nums))
        return first + len(nums) - 1 - last - (first > last)
