class Solution:
    def averageValue(self, nums: list[int]) -> int:
        values = [value for value in nums if value % 6 == 0]
        return sum(values) // len(values) if values else 0
