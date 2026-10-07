class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = {(0, 0): grid[0][0]}
        for step in range(1, 2 * n - 1):
            nxt = {}
            for r1 in range(max(0, step - n + 1), min(n, step + 1)):
                c1 = step - r1
                if grid[r1][c1] == -1:
                    continue
                for r2 in range(max(0, step - n + 1), min(n, step + 1)):
                    c2 = step - r2
                    if grid[r2][c2] == -1:
                        continue
                    best = max(
                        dp.get((r1 - a, r2 - b), -(10**9))
                        for a in (0, 1)
                        for b in (0, 1)
                    )
                    if best >= 0:
                        nxt[r1, r2] = (
                            best + grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)
                        )
            dp = nxt
        return dp.get((n - 1, n - 1), 0)
