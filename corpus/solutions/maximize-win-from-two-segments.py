class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        best_prefix = [0] * len(prizePositions)
        left = 0
        best = 0
        for right, position in enumerate(prizePositions):
            while position - prizePositions[left] > k:
                left += 1
            current = right - left + 1
            previous = best_prefix[left - 1] if left else 0
            best = max(best, previous + current)
            best_prefix[right] = max(best_prefix[right - 1] if right else 0, current)
        return best
