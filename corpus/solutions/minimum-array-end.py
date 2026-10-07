class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining = n - 1
        answer = x
        bit = 0
        while remaining:
            if (x >> bit) & 1 == 0:
                if remaining & 1:
                    answer |= 1 << bit
                remaining >>= 1
            bit += 1
        return answer
