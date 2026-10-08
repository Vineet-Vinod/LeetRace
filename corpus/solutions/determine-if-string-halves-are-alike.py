class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        middle = len(s) // 2
        return sum(char in vowels for char in s[:middle]) == sum(
            char in vowels for char in s[middle:]
        )
