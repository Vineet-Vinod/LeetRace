class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        p = 1
        while p <= n:
            ans += (n // (p * 10)) * p + min(p, max(0, n % (p * 10) - p + 1))
            p *= 10
        return ans
