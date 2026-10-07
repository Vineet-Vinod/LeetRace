class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted({int(char) for char in s if char.isdigit()}, reverse=True)
        return digits[1] if len(digits) >= 2 else -1
