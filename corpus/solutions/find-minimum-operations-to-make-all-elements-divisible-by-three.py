class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(value % 3 != 0 for value in nums)
