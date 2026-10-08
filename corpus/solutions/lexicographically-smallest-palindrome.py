class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        for i in range(len(chars) // 2):
            chars[-1 - i] = chars[i] = min(chars[i], chars[-1 - i])
        return "".join(chars)
