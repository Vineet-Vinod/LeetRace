class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)
        for r in range(n):
            for c in range(n):
                height = grid[r][c]
                if height:
                    area += 2 + 4 * height
                if r:
                    area -= 2 * min(height, grid[r - 1][c])
                if c:
                    area -= 2 * min(height, grid[r][c - 1])
        return area
