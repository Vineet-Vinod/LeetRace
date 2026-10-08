class Solution:
    def compressedString(self, word: str) -> str:
        out = []
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i] and j - i < 9:
                j += 1
            out.extend((str(j - i), word[i]))
            i = j
        return "".join(out)
