from fractions import Fraction


class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def search(values: tuple[Fraction, ...]) -> bool:
            if len(values) == 1:
                return values[0] == 24
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    a, b = values[i], values[j]
                    rest = tuple(x for k, x in enumerate(values) if k != i and k != j)
                    options = {a + b, a - b, b - a, a * b}
                    if b:
                        options.add(a / b)
                    if a:
                        options.add(b / a)
                    if any(search(rest + (x,)) for x in options):
                        return True
            return False

        return search(tuple(Fraction(x) for x in cards))
