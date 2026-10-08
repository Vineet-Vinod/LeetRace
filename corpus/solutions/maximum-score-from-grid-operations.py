from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[-(10**30)] * (n + 1) for _ in range(n + 1)]
        dp[0] = [0] * (n + 1)
        for j in range(n):
            p = [0]
            for i in range(n):
                p.append(p[-1] + grid[i][j])
            nxt = [[-(10**30)] * (n + 1) for _ in range(n + 1)]
            for b in range(n + 1):
                prefix = []
                best = -(10**30)
                for a in range(n + 1):
                    best = max(best, dp[a][b])
                    prefix.append(best)
                suffix = [-(10**30)] * (n + 2)
                for a in range(n, -1, -1):
                    suffix[a] = max(suffix[a + 1], dp[a][b] + p[a] - p[b])
                for c in range(n + 1):
                    bound = max(b, c)
                    nxt[b][c] = max(
                        prefix[bound] + max(0, p[c] - p[b]), suffix[bound + 1]
                    )
            dp = nxt
        return max(dp[b][0] for b in range(n + 1))
