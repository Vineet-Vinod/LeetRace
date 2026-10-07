class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = Counter(s)
        return sum(count * (count + 1) // 2 for count in counts.values())
