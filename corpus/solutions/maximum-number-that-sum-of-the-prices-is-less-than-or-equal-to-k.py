class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def accumulated_price(number: int) -> int:
            total = 0
            bit = x - 1
            while (1 << bit) <= number:
                cycle = 1 << (bit + 1)
                half = 1 << bit
                total += (number + 1) // cycle * half
                remainder = (number + 1) % cycle
                total += max(0, remainder - half)
                bit += x
            return total

        low, high = 0, 1 << 62
        while low < high:
            middle = (low + high + 1) // 2
            if accumulated_price(middle) <= k:
                low = middle
            else:
                high = middle - 1
        return low
