class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, min(x, 46340)
        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= x:
                left = middle + 1
            else:
                right = middle - 1
        return right
