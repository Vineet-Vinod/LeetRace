class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        first = Counter(word1)
        second = Counter(word2)
        return all(
            abs(first[char] - second[char]) <= 3 for char in string.ascii_lowercase
        )
