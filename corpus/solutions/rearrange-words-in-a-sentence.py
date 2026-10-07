class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key=len)
        result = " ".join(words)
        return result[:1].upper() + result[1:]
