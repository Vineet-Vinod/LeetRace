class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ordered = sorted(piles, reverse=True)
        groups = len(piles) // 3
        return sum(ordered[1 : 2 * groups : 2])
