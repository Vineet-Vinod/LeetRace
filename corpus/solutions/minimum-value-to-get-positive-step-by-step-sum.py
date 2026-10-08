class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix = 0
        minimum = 0
        for value in nums:
            prefix += value
            minimum = min(minimum, prefix)
        return 1 - minimum
