class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ends = [0] * 26
        total = 0
        for c in s:
            i = ord(c) - 97
            new = (total + 1) % 1000000007
            total = (total + new - ends[i]) % 1000000007
            ends[i] = new
        return total
