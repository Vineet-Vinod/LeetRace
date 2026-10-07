class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = list(Counter(s).values())
        return all(count == counts[0] for count in counts)
