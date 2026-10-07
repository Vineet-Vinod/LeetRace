class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = iter(char for char in reversed(s) if char.isalpha())
        return "".join(next(letters) if char.isalpha() else char for char in s)
