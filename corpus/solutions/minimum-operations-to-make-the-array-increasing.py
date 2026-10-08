class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        previous = nums[0]
        for value in nums[1:]:
            required = previous + 1
            if value < required:
                operations += required - value
                value = required
            previous = value
        return operations
