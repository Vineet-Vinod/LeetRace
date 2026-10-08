class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(not any(char in broken for char in word) for word in text.split())
