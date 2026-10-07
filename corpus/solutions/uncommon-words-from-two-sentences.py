class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter((s1 + " " + s2).split())
        return sorted(word for word, count in counts.items() if count == 1)
