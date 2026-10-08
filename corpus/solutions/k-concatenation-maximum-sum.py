class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        repetitions = min(k, 2)
        best = 0
        current = 0
        for value in arr * repetitions:
            current = max(0, current + value)
            best = max(best, current)
        total = sum(arr)
        if k > 2 and total > 0:
            best += (k - 2) * total
        return best % mod
