class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        return sum(value - minimum for value in nums)
