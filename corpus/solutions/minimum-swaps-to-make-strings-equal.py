class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = sum(a == "x" and b == "y" for a, b in zip(s1, s2))
        yx = sum(a == "y" and b == "x" for a, b in zip(s1, s2))
        if (xy + yx) % 2:
            return -1
        return xy // 2 + yx // 2 + 2 * (xy % 2)
