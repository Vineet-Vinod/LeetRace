class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        best = run = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                run += 1
            else:
                run = 1
            best = max(best, run)
        return best
