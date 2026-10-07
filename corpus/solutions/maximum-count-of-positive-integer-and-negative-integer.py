class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(value < 0 for value in nums), sum(value > 0 for value in nums))
