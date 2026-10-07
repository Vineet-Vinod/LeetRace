class Solution:
    def addMinimum(self, word: str) -> int:
        groups = 1
        for index in range(1, len(word)):
            if word[index] <= word[index - 1]:
                groups += 1
        return groups * 3 - len(word)
