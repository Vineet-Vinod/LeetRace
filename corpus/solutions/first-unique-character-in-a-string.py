class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        return next((i for i, char in enumerate(s) if counts[char] == 1), -1)
