class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        row_hits = 0
        col_hits = [0] * cols
        for r in range(rows):
            for c in range(cols):
                if c == 0 or grid[r][c - 1] == "W":
                    row_hits = 0
                    j = c
                    while j < cols and grid[r][j] != "W":
                        row_hits += grid[r][j] == "E"
                        j += 1
                if r == 0 or grid[r - 1][c] == "W":
                    col_hits[c] = 0
                    j = r
                    while j < rows and grid[j][c] != "W":
                        col_hits[c] += grid[j][c] == "E"
                        j += 1
                if grid[r][c] == "0":
                    best = max(best, row_hits + col_hits[c])
        return best
