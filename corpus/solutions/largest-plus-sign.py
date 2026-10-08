class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        blocked = {r * n + c for r, c in mines}
        arms = [[n] * n for _ in range(n)]
        for r in range(n):
            run = 0
            for c in range(n):
                run = 0 if r * n + c in blocked else run + 1
                arms[r][c] = run
            run = 0
            for c in range(n - 1, -1, -1):
                run = 0 if r * n + c in blocked else run + 1
                arms[r][c] = min(arms[r][c], run)
        best = 0
        for c in range(n):
            run = 0
            for r in range(n):
                run = 0 if r * n + c in blocked else run + 1
                arms[r][c] = min(arms[r][c], run)
            run = 0
            for r in range(n - 1, -1, -1):
                run = 0 if r * n + c in blocked else run + 1
                arms[r][c] = min(arms[r][c], run)
                best = max(best, arms[r][c])
        return best
