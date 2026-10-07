class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        mismatch = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        if len(mismatch) % 2:
            return -1
        total = 0
        for i in range(1, len(mismatch), 2):
            total += min(x, mismatch[i] - mismatch[i - 1])
        return total
