from __future__ import annotations
from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        size = {}
        answer = []
        count = 0

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for r, c in positions:
            cell = r * n + c
            if cell not in parent:
                parent[cell] = cell
                size[cell] = 1
                count += 1
                for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    other = a * n + b
                    if 0 <= a < m and 0 <= b < n and other in parent:
                        x, y = find(cell), find(other)
                        if x != y:
                            if size[x] < size[y]:
                                x, y = y, x
                            parent[y] = x
                            size[x] += size[y]
                            count -= 1
            answer.append(count)
        return answer
