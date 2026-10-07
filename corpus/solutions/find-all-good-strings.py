class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10**9 + 7
        m = len(evil)
        failure = [0] * m
        for i in range(1, m):
            j = failure[i - 1]
            while j and evil[j] != evil[i]:
                j = failure[j - 1]
            if evil[j] == evil[i]:
                j += 1
            failure[i] = j
        trans = [[0] * 26 for _ in range(m)]
        for j in range(m):
            for c in range(26):
                ch = chr(97 + c)
                k = j
                while k and evil[k] != ch:
                    k = failure[k - 1]
                if evil[k] == ch:
                    k += 1
                trans[j][c] = k
        dp = {(0, True, True): 1}
        for i in range(n):
            nxt = {}
            for (matched, lo, hi), count in dp.items():
                for c in range(
                    ord(s1[i]) - 97 if lo else 0, (ord(s2[i]) - 97 if hi else 25) + 1
                ):
                    k = trans[matched][c]
                    if k == m:
                        continue
                    key = (k, lo and c == ord(s1[i]) - 97, hi and c == ord(s2[i]) - 97)
                    nxt[key] = (nxt.get(key, 0) + count) % mod
            dp = nxt
        return sum(dp.values()) % mod
