class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == "-":
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        for i, digit in enumerate(n):
            if int(digit) < x:
                return n[:i] + str(x) + n[i:]
        return n + str(x)
