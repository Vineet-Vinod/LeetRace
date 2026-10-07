class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        return sum(value for index, value in enumerate(nums) if index.bit_count() == k)
