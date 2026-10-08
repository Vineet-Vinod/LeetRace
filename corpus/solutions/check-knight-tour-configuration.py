class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        positions = [None] * (n * n)
        for row in range(n):
            for col in range(n):
                positions[grid[row][col]] = (row, col)
        for move in range(1, n * n):
            r1, c1 = positions[move - 1]
            r2, c2 = positions[move]
            if sorted((abs(r2 - r1), abs(c2 - c1))) != [1, 2]:
                return False
        return True
