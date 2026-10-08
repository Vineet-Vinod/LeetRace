from functools import lru_cache


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def solve(s):
            if s == s2:
                return 0
            i = next(i for i in range(len(s)) if s[i] != s2[i])
            best = len(s)
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    chars = list(s)
                    chars[i], chars[j] = chars[j], chars[i]
                    best = min(best, 1 + solve("".join(chars)))
            return best

        return solve(s1)
