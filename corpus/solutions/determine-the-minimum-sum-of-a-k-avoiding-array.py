class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        low_count = min(n, k // 2)
        low_sum = low_count * (low_count + 1) // 2
        remaining = n - low_count
        high_sum = remaining * (2 * k + remaining - 1) // 2
        return low_sum + high_sum
