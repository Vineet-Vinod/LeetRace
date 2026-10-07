class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        for a, b, mid in [
            (1, 3, 2),
            (1, 7, 4),
            (3, 9, 6),
            (7, 9, 8),
            (1, 9, 5),
            (3, 7, 5),
            (2, 8, 5),
            (4, 6, 5),
        ]:
            skip[a][b] = skip[b][a] = mid
        used = [False] * 10

        def count(last: int, length: int) -> int:
            if length > n:
                return 0
            total = int(length >= m)
            for nxt in range(1, 10):
                mid = skip[last][nxt]
                if not used[nxt] and (mid == 0 or used[mid]):
                    used[nxt] = True
                    total += count(nxt, length + 1)
                    used[nxt] = False
            return total

        return count(0, 0)
