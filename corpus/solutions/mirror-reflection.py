class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common = gcd(p, q)
        horizontal, vertical = p // common, q // common
        if horizontal % 2 == 0:
            return 2
        return 1 if vertical % 2 else 0
