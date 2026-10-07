class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        value = num & 0xFFFFFFFF
        digits = "0123456789abcdef"
        result = ""
        while value:
            result = digits[value & 15] + result
            value >>= 4
        return result
