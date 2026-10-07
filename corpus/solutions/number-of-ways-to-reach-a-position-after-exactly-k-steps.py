class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        distance = abs(endPos - startPos)
        if distance > k or (k - distance) % 2:
            return 0
        return comb(k, (k + distance) // 2) % (10**9 + 7)
