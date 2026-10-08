class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        previous = list(range(len(word2) + 1))
        for row, char1 in enumerate(word1, 1):
            current = [row] + [0] * len(word2)
            for col, char2 in enumerate(word2, 1):
                current[col] = min(
                    previous[col] + 1,
                    current[col - 1] + 1,
                    previous[col - 1] + (char1 != char2),
                )
            previous = current
        return previous[-1]
