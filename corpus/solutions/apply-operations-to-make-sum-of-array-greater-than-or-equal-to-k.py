class Solution:
    def minOperations(self, k: int) -> int:
        best = k - 1
        for increments in range(k):
            duplicates = (k + increments) // (increments + 1) - 1
            best = min(best, increments + duplicates)
            if increments >= best:
                break
        return best
