class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        pal = [bytearray(n) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            pal[i][i] = 1
            for j in range(i + 1, n):
                pal[i][j] = s[i] == s[j] and (j - i == 1 or pal[i + 1][j - 1])
        for i in range(n - 2):
            if pal[0][i]:
                for j in range(i + 1, n - 1):
                    if pal[i + 1][j] and pal[j + 1][n - 1]:
                        return True
        return False
