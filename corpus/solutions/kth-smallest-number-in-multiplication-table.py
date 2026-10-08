class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        m, n = min(m, n), max(m, n)
        low, high = 1, m * n
        while low < high:
            middle = (low + high) // 2
            count = sum(min(n, middle // i) for i in range(1, m + 1))
            if count >= k:
                high = middle
            else:
                low = middle + 1
        return low
