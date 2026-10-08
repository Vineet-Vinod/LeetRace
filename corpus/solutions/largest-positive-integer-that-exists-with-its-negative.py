class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        values = set(nums)
        return max(
            (value for value in values if value > 0 and -value in values), default=-1
        )
