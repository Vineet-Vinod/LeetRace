class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        xor = 0
        for pile in piles:
            xor ^= pile
        return xor != 0
