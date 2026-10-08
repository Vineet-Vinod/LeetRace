from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        placed = []
        out = []
        best = 0
        for left, side in positions:
            height = side + max(
                (h for a, b, h in placed if a < left + side and left < b), default=0
            )
            placed.append((left, left + side, height))
            best = max(best, height)
            out.append(best)
        return out
