class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = [r for r, row in enumerate(grid) for value in row if value]
        cols = sorted(c for row in grid for c, value in enumerate(row) if value)
        return sum(abs(r - rows[len(rows) // 2]) for r in rows) + sum(
            abs(c - cols[len(cols) // 2]) for c in cols
        )
