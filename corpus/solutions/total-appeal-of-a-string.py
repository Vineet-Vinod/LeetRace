class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        total = 0
        for i, c in enumerate(s):
            total += (i - last.get(c, -1)) * (len(s) - i)
            last[c] = i
        return total
