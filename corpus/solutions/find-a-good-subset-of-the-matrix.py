from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        first = {}
        for i, row in enumerate(grid):
            mask = sum(value << bit for bit, value in enumerate(row))
            if mask == 0:
                return [i]
            if mask not in first:
                first[mask] = i
        best = None
        for left, i in first.items():
            for right, j in first.items():
                if left & right == 0:
                    pair = sorted((i, j))
                    if best is None or pair < best:
                        best = pair
        return best if best is not None else []
