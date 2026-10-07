class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = Counter(s[i : i + 10] for i in range(len(s) - 9))
        return sorted(sequence for sequence, count in counts.items() if count > 1)
