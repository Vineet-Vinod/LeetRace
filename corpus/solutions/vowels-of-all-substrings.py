class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = set("aeiou")
        return sum((i + 1) * (n - i) for i, ch in enumerate(word) if ch in vowels)
