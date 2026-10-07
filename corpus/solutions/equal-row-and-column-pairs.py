class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        total = 0
        for c in range(len(grid)):
            column = tuple(grid[r][c] for r in range(len(grid)))
            total += rows[column]
        return total
