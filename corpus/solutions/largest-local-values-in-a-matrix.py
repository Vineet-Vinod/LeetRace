class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [
            [
                max(grid[i + x][j + y] for x in range(3) for y in range(3))
                for j in range(n - 2)
            ]
            for i in range(n - 2)
        ]
