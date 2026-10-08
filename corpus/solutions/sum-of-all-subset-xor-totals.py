class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combined = 0
        for value in nums:
            combined |= value
        return combined << (len(nums) - 1)
