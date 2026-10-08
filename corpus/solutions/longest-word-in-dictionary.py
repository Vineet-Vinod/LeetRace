class Solution:
    def longestWord(self, words: List[str]) -> str:
        available = set(words)
        best = ""
        for word in sorted(words):
            if all(word[:length] in available for length in range(1, len(word))):
                if len(word) > len(best):
                    best = word
        return best
