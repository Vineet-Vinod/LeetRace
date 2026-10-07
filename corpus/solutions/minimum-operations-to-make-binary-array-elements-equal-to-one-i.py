class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        values = nums.copy()
        for index in range(len(values) - 2):
            if values[index] == 0:
                values[index] ^= 1
                values[index + 1] ^= 1
                values[index + 2] ^= 1
                operations += 1
        return operations if all(values) else -1
