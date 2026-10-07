class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if i + 1 < len(grid) and grid[i + 1][j] != value:
                    return False
                if j + 1 < len(row) and row[j + 1] == value:
                    return False
        return True
