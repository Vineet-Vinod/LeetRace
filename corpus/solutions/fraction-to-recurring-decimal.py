class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        negative = (numerator < 0) != (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        whole, remainder = divmod(numerator, denominator)
        result = ("-" if negative else "") + str(whole)
        if remainder == 0:
            return result
        result += "."
        positions: Dict[int, int] = {}
        digits: List[str] = []
        while remainder and remainder not in positions:
            positions[remainder] = len(digits)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            digits.append(str(digit))
        if remainder:
            repeat_start = positions[remainder]
            return (
                result
                + "".join(digits[:repeat_start])
                + "("
                + "".join(digits[repeat_start:])
                + ")"
            )
        return result + "".join(digits)
