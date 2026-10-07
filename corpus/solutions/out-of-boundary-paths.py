class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7
        current = [[0] * n for _ in range(m)]
        current[startRow][startColumn] = 1
        answer = 0
        for _ in range(maxMove):
            following = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    ways = current[r][c]
                    if not ways:
                        continue
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            following[nr][nc] = (following[nr][nc] + ways) % mod
                        else:
                            answer = (answer + ways) % mod
            current = following
        return answer
