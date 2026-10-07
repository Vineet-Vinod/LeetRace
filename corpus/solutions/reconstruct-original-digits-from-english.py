class Solution:
    def originalDigits(self, s: str) -> str:
        counts = Counter(s)
        digits = [0] * 10
        digits[0] = counts["z"]
        digits[2] = counts["w"]
        digits[4] = counts["u"]
        digits[6] = counts["x"]
        digits[8] = counts["g"]
        digits[3] = counts["h"] - digits[8]
        digits[5] = counts["f"] - digits[4]
        digits[7] = counts["s"] - digits[6]
        digits[1] = counts["o"] - digits[0] - digits[2] - digits[4]
        digits[9] = counts["i"] - digits[5] - digits[6] - digits[8]
        return "".join(str(digit) * amount for digit, amount in enumerate(digits))
