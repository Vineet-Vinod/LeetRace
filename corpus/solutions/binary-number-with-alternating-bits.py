class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = n ^ (n >> 1)
        return (bits & (bits + 1)) == 0
