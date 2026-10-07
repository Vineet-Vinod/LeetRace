class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        first = grid[0]
        return all(
            row == first or row == [1 - value for value in first] for row in grid
        )
