class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits: list[str] = []
        for digit in num:
            while k and digits and digits[-1] > digit:
                digits.pop()
                k -= 1
            digits.append(digit)
        if k:
            digits = digits[:-k]
        result = "".join(digits).lstrip("0")
        return result or "0"
