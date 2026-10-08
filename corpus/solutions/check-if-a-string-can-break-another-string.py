class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        first = sorted(s1)
        second = sorted(s2)
        first_breaks = all(a >= b for a, b in zip(first, second))
        second_breaks = all(b >= a for a, b in zip(first, second))
        return first_breaks or second_breaks
