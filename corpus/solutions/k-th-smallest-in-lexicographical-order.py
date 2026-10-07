class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        k -= 1
        while k:
            first, after = prefix, prefix + 1
            size = 0
            while first <= n:
                size += min(n + 1, after) - first
                first *= 10
                after *= 10
            if size <= k:
                prefix += 1
                k -= size
            else:
                prefix *= 10
                k -= 1
        return prefix
