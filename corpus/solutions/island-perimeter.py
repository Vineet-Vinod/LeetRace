class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    perimeter += (
                        4 - 2 * (i > 0 and grid[i - 1][j]) - 2 * (j > 0 and row[j - 1])
                    )
        return perimeter
