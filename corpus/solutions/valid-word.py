class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum() or not word.isascii():
            return False
        vowels = set("aeiouAEIOU")
        return any(char in vowels for char in word) and any(
            char.isalpha() and char not in vowels for char in word
        )
