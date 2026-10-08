class Solution:
    def toHexspeak(self, num: str) -> str:
        digits = format(int(num), "X")
        if any(char not in "0123456789ABCDEF" for char in digits):
            return "ERROR"
        translated = digits.replace("0", "O").replace("1", "I")
        return translated if all(char in "ABCDEFIO" for char in translated) else "ERROR"
