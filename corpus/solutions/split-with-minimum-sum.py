class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        first = "".join(digits[::2])
        second = "".join(digits[1::2])
        return int(first or "0") + int(second or "0")
