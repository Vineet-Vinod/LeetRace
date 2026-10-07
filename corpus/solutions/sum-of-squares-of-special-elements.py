class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        size = len(nums)
        return sum(
            value * value for index, value in enumerate(nums, 1) if size % index == 0
        )
