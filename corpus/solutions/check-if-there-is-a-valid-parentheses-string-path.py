class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        states = [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                before = states[j] | (states[j - 1] if j else set())
                if i == j == 0:
                    before = {0}
                delta = 1 if grid[i][j] == "(" else -1
                remaining = m + n - i - j - 2
                states[j] = {v + delta for v in before if 0 <= v + delta <= remaining}
        return 0 in states[-1]
