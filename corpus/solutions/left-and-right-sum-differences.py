class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left = 0
        result = []
        for value in nums:
            result.append(abs(left - (total - left - value)))
            left += value
        return result
