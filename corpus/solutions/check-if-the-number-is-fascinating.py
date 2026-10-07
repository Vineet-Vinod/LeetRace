class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = str(n) + str(2 * n) + str(3 * n)
        return len(digits) == 9 and set(digits) == set("123456789")
