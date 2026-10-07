class Solution:
    def maxA(self, n: int) -> int:
        best = [0] * (n + 1)
        for presses in range(1, n + 1):
            best[presses] = best[presses - 1] + 1
            for start in range(1, presses - 2):
                best[presses] = max(best[presses], best[start] * (presses - start - 1))
        return best[n]
