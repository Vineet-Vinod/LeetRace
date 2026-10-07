class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] in "+-":
                sign = -1 if expression[i] == "-" else 1
                i += 1
            j = expression.index("/", i)
            top = sign * int(expression[i:j])
            i = j + 1
            j = i
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            bottom = int(expression[i:j])
            numerator = numerator * bottom + top * denominator
            denominator *= bottom
            divisor = gcd(abs(numerator), denominator)
            numerator //= divisor
            denominator //= divisor
            i = j
        return f"{numerator}/{denominator}"
