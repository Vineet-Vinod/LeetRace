class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((a - b) % 2 != 0 for a, b in zip(nums, nums[1:]))
