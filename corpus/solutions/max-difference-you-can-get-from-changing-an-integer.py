class Solution:
    def maxDiff(self, num: int) -> int:
        digits = list(str(num))
        high = digits[:]
        for digit in digits:
            if digit != "9":
                high = ["9" if value == digit else value for value in digits]
                break
        low = digits[:]
        if digits[0] != "1":
            target = digits[0]
            low = ["1" if value == target else value for value in digits]
        else:
            for digit in digits[1:]:
                if digit not in ("0", "1"):
                    low = ["0" if value == digit else value for value in digits]
                    break
        return int("".join(high)) - int("".join(low))
