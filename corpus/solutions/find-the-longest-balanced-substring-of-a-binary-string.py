class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        index = 0
        while index < len(s):
            if s[index] == "1":
                index += 1
                continue
            zeros = 0
            while index < len(s) and s[index] == "0":
                zeros += 1
                index += 1
            ones = 0
            while index < len(s) and s[index] == "1":
                ones += 1
                index += 1
            best = max(best, 2 * min(zeros, ones))
        return best
