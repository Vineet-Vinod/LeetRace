class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(word: str) -> int:
            result = 0
            for char in word:
                result = result * 10 + ord(char) - ord("a")
            return result

        return value(firstWord) + value(secondWord) == value(targetWord)
