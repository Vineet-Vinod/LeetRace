class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(value * value for value in nums)
