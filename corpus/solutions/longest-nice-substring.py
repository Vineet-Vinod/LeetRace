class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ""
        for left in range(len(s)):
            lower = set()
            upper = set()
            for right in range(left, len(s)):
                ch = s[right]
                if ch.islower():
                    lower.add(ch)
                else:
                    upper.add(ch.lower())
                if lower == upper and right - left + 1 > len(best):
                    best = s[left : right + 1]
        return best
