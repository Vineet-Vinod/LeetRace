class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        operations = 0
        for value in nums:
            if value ^ flips == 0:
                flips ^= 1
                operations += 1
        return operations
