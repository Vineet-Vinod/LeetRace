class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = [
            f"{numerator}/{denominator}"
            for denominator in range(2, n + 1)
            for numerator in range(1, denominator)
            if gcd(numerator, denominator) == 1
        ]
        return sorted(fractions)
