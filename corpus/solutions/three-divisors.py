class Solution:
    def isThree(self, n: int) -> bool:
        root = math.isqrt(n)
        if root < 2 or root * root != n:
            return False
        return all(root % divisor != 0 for divisor in range(2, math.isqrt(root) + 1))
