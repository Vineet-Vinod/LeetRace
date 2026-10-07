class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        start = 0
        total = 0
        for index, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char] + 1)
            last_seen[char] = index
            total += index - start + 1
        return total
