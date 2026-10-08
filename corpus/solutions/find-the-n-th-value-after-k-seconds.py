class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return comb(n + k - 1, k) % (10**9 + 7)
