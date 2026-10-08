from math import isqrt


class Solution:
    def minimumBoxes(self, n: int) -> int:
        low, high = 0, 2000
        while low < high:
            mid = (low + high + 1) // 2
            if mid * (mid + 1) * (mid + 2) // 6 <= n:
                low = mid
            else:
                high = mid - 1
        h = low
        remaining = n - h * (h + 1) * (h + 2) // 6
        extra = (isqrt(8 * remaining + 1) - 1) // 2
        if extra * (extra + 1) // 2 < remaining:
            extra += 1
        return h * (h + 1) // 2 + extra
