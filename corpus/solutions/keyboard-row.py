class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
        result = []
        for word in words:
            lowered = word.lower()
            if any(set(lowered) <= row for row in rows):
                result.append(word)
        return result
