class Solution:
    def oddString(self, words: List[str]) -> str:
        keys = [
            tuple(ord(b) - ord(a) for a, b in zip(word, word[1:])) for word in words
        ]
        counts = Counter(keys)
        return words[next(i for i, key in enumerate(keys) if counts[key] == 1)]
