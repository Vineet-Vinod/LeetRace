class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(value % 2 == 0 for value in nums) >= 2
