class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        values = sorted(nums)
        return values[-1] * values[-2] - values[0] * values[1]
