from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        best = [0] * len(costs[0])
        for row in costs:
            first, second = sorted(range(len(best)), key=best.__getitem__)[:2]
            best = [
                cost + best[second if color == first else first]
                for color, cost in enumerate(row)
            ]
        return min(best)
