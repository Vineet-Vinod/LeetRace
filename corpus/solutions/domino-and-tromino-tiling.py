class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 1
        full_two_back = 1
        full_one_back = 1
        partial_one_back = 0
        for _ in range(2, n + 1):
            full = (full_one_back + full_two_back + 2 * partial_one_back) % mod
            partial = (partial_one_back + full_two_back) % mod
            full_two_back, full_one_back, partial_one_back = (
                full_one_back,
                full,
                partial,
            )
        return full_one_back
