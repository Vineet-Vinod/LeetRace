class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return next(
            i
            for i, row in enumerate(grid)
            if all(row[j] == 1 for j in range(len(grid)) if j != i)
        )
