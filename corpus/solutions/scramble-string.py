from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def solve(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            for split in range(1, len(a)):
                if solve(a[:split], b[:split]) and solve(a[split:], b[split:]):
                    return True
                if solve(a[:split], b[-split:]) and solve(a[split:], b[:-split]):
                    return True
            return False

        return solve(s1, s2)
