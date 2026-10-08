class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        for count in Counter(nums).values():
            if count == 1:
                return -1
            operations += (count + 2) // 3
        return operations
