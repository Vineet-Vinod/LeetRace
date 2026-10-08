class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = sum(value.bit_count() for value in nums)
        doublings = max((value.bit_length() - 1 for value in nums), default=0)
        return increments + doublings
