class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        items = sorted(value for row in values for value in row)
        return sum(day * value for day, value in enumerate(items, 1))
