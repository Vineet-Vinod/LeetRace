class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        values = nums[:]
        while len(values) > 1:
            values = [(values[i] + values[i + 1]) % 10 for i in range(len(values) - 1)]
        return values[0]
