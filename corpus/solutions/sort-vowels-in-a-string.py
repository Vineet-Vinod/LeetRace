class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ordered = iter(sorted(char for char in s if char in vowels))
        return "".join(next(ordered) if char in vowels else char for char in s)
