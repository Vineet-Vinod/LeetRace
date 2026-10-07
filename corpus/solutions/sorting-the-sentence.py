class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ordered = [""] * len(words)
        for word in words:
            ordered[int(word[-1]) - 1] = word[:-1]
        return " ".join(ordered)
