class Solution:
    def countDistinct(self, s: str) -> int:
        substrings = set()
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substrings.add(s[start:end])
        return len(substrings)
