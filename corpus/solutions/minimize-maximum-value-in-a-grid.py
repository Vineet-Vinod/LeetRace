from __future__ import annotations
from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        answer = [[0] * n for _ in range(m)]
        for value, r, c in sorted(
            (grid[r][c], r, c) for r in range(m) for c in range(n)
        ):
            score = max(rows[r], cols[c]) + 1
            answer[r][c] = score
            rows[r] = cols[c] = score
        return answer
