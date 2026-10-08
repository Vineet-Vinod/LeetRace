class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counts: dict[frozenset[str], int] = {}
        pairs = 0
        for word in words:
            letters = frozenset(word)
            pairs += counts.get(letters, 0)
            counts[letters] = counts.get(letters, 0) + 1
        return pairs
