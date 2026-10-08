class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            middle = (left + right) // 2
            stores = sum((amount + middle - 1) // middle for amount in quantities)
            if stores <= n:
                right = middle
            else:
                left = middle + 1
        return left
