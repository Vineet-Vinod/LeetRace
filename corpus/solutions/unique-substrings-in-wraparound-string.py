class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        best = [0] * 26
        run = 0
        for i, ch in enumerate(s):
            if i and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                run += 1
            else:
                run = 1
            idx = ord(ch) - 97
            best[idx] = max(best[idx], run)
        return sum(best)
