class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(value < 0 for row in grid for value in row)
