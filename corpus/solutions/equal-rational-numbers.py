from fractions import Fraction


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(text):
            integer, dot, decimal = text.partition(".")
            result = Fraction(int(integer))
            finite, marker, repeating = decimal.partition("(")
            scale = 10 ** len(finite)
            if finite:
                result += Fraction(int(finite), scale)
            if marker:
                repeating = repeating[:-1]
                result += Fraction(int(repeating), scale * (10 ** len(repeating) - 1))
            return result

        return parse(s) == parse(t)
