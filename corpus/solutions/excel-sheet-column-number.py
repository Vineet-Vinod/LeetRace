class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value = 0
        for ch in columnTitle:
            value = value * 26 + ord(ch) - 64
        return value
