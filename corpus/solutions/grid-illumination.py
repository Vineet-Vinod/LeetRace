from collections import Counter


class Solution:
    def gridIllumination(
        self, n: int, lamps: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        active = set(map(tuple, lamps))
        rows = Counter(x for x, y in active)
        cols = Counter(y for x, y in active)
        diag = Counter(x - y for x, y in active)
        anti = Counter(x + y for x, y in active)
        answer = []
        for x, y in queries:
            answer.append(int(bool(rows[x] or cols[y] or diag[x - y] or anti[x + y])))
            for a in range(x - 1, x + 2):
                for b in range(y - 1, y + 2):
                    if (a, b) in active:
                        active.remove((a, b))
                        rows[a] -= 1
                        cols[b] -= 1
                        diag[a - b] -= 1
                        anti[a + b] -= 1
        return answer
