from functools import cache


class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        def solve(g: list[list[int]]) -> int:
            m, n = len(g), len(g[0])

            @cache
            def area(r0: int, r1: int, c0: int, c1: int) -> int:
                top, bottom, left, right = m, -1, n, -1
                for r in range(r0, r1):
                    for c in range(c0, c1):
                        if g[r][c]:
                            top, bottom = min(top, r), max(bottom, r)
                            left, right = min(left, c), max(right, c)
                return (bottom - top + 1) * (right - left + 1) if bottom >= 0 else 10**9

            best = 10**9
            for r in range(1, m):
                for s in range(r + 1, m):
                    best = min(
                        best, area(0, r, 0, n) + area(r, s, 0, n) + area(s, m, 0, n)
                    )
                for c in range(1, n):
                    best = min(
                        best,
                        area(0, r, 0, n) + area(r, m, 0, c) + area(r, m, c, n),
                        area(0, r, 0, c) + area(0, r, c, n) + area(r, m, 0, n),
                    )
            return best

        return min(solve(grid), solve([list(row) for row in zip(*grid)]))
