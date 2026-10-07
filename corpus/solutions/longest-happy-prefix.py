class Solution:
    def longestPrefix(self, s: str) -> str:
        pi = [0] * len(s)
        for i in range(1, len(s)):
            j = pi[i - 1]
            while j and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return s[: pi[-1]]
