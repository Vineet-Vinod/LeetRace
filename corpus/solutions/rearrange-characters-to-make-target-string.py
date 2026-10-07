class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter

        available = Counter(s)
        needed = Counter(target)
        return min(available[ch] // count for ch, count in needed.items())
