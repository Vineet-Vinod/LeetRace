class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))
        return "".join(chars)
