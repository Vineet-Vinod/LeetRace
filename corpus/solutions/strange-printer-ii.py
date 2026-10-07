from __future__ import annotations
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        bounds = {}
        for r in range(m):
            for c in range(n):
                color = targetGrid[r][c]
                if color not in bounds:
                    bounds[color] = [r, r, c, c]
                box = bounds[color]
                box[0], box[1] = min(box[0], r), max(box[1], r)
                box[2], box[3] = min(box[2], c), max(box[3], c)
        adj = {color: set() for color in bounds}
        indegree = {color: 0 for color in bounds}
        for color, (top, bottom, left, right) in bounds.items():
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    other = targetGrid[r][c]
                    if other != color and other not in adj[color]:
                        adj[color].add(other)
                        indegree[other] += 1
        queue = [c for c in indegree if indegree[c] == 0]
        for color in queue:
            for other in adj[color]:
                indegree[other] -= 1
                if indegree[other] == 0:
                    queue.append(other)
        return len(queue) == len(bounds)
