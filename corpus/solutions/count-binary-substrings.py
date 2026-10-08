class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        run = 1
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                run += 1
            else:
                total += min(prev, run)
                prev, run = run, 1
        return total + min(prev, run)
