class Solution:
    def minDeletions(self, s: str) -> int:
        used = set()
        deletions = 0
        for frequency in Counter(s).values():
            while frequency and frequency in used:
                frequency -= 1
                deletions += 1
            if frequency:
                used.add(frequency)
        return deletions
