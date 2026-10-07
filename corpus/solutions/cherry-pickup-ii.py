class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = {(0, n - 1): grid[0][0] + grid[0][-1]}
        for row in grid[1:]:
            nxt = {}
            for (a, b), value in dp.items():
                for x in range(max(0, a - 1), min(n, a + 2)):
                    for y in range(max(0, b - 1), min(n, b + 2)):
                        score = value + row[x] + (row[y] if x != y else 0)
                        nxt[x, y] = max(nxt.get((x, y), -1), score)
            dp = nxt
        return max(dp.values())
