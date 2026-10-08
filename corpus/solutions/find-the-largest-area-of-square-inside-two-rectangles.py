class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        best_side = 0
        for first in range(len(bottomLeft)):
            for second in range(first + 1, len(bottomLeft)):
                width = min(topRight[first][0], topRight[second][0]) - max(
                    bottomLeft[first][0], bottomLeft[second][0]
                )
                height = min(topRight[first][1], topRight[second][1]) - max(
                    bottomLeft[first][1], bottomLeft[second][1]
                )
                best_side = max(best_side, min(width, height))
        return best_side * best_side
