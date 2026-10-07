class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(value > 0 for row in grid for value in row)
        front = sum(max(row) for row in grid)
        side = sum(
            max(grid[row][column] for row in range(len(grid)))
            for column in range(len(grid))
        )
        return top + front + side
