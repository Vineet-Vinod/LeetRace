class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        reachable = [True] * rows
        for c in range(1, cols):
            next_reachable = [False] * rows
            for r in range(rows):
                if (
                    (r > 0 and reachable[r - 1] and grid[r - 1][c - 1] < grid[r][c])
                    or (reachable[r] and grid[r][c - 1] < grid[r][c])
                    or (
                        r + 1 < rows
                        and reachable[r + 1]
                        and grid[r + 1][c - 1] < grid[r][c]
                    )
                ):
                    next_reachable[r] = True
            if not any(next_reachable):
                return c - 1
            reachable = next_reachable
        return cols - 1
