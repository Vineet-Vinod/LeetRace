class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        length = len(nums)
        return sum(
            (ones := sum((value >> bit) & 1 for value in nums)) * (length - ones)
            for bit in range(31)
        )
