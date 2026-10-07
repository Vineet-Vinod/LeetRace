class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        import math

        n = numPeople // 2
        return (math.comb(2 * n, n) // (n + 1)) % (10**9 + 7)
