class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[1] * n for _ in range(m)]
        mod = 10**9 + 7
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        for value, i, j in cells:
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > value:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod
        return sum(map(sum, dp)) % mod
