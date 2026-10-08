class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current = sum(char in vowels for char in s[:k])
        best = current
        for i in range(k, len(s)):
            current += (s[i] in vowels) - (s[i - k] in vowels)
            best = max(best, current)
        return best
