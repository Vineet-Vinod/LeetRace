class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = []
        total = 0
        for x in stones:
            total += x
            prefix.append(total)
        best = prefix[-1]
        for i in range(len(stones) - 2, 0, -1):
            best = max(best, prefix[i] - best)
        return best
