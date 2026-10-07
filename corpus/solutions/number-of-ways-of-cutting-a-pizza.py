from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        from functools import lru_cache

        rows, cols = len(pizza), len(pizza[0])
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (
                    (pizza[r][c] == "A")
                    + apples[r + 1][c]
                    + apples[r][c + 1]
                    - apples[r + 1][c + 1]
                )

        @lru_cache(None)
        def count(r, c, pieces):
            if apples[r][c] < pieces:
                return 0
            if pieces == 1:
                return 1
            answer = 0
            for nr in range(r + 1, rows):
                if apples[r][c] > apples[nr][c]:
                    answer += count(nr, c, pieces - 1)
            for nc in range(c + 1, cols):
                if apples[r][c] > apples[r][nc]:
                    answer += count(r, nc, pieces - 1)
            return answer % (10**9 + 7)

        return count(0, 0, k)
