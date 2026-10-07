class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = False
        while n > 1:
            middle = 1 << (n - 1)
            if k == middle:
                return "0" if invert else "1"
            if k > middle:
                k = (1 << n) - k
                invert = not invert
            n -= 1
        return "1" if invert else "0"
