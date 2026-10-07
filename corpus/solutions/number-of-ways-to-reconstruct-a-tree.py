from __future__ import annotations
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = {}
        for a, b in pairs:
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)
        root = next((a for a in adj if len(adj[a]) == len(adj) - 1), None)
        if root is None:
            return 0
        answer = 1
        for node, neighbors in adj.items():
            if node == root:
                continue
            possible = [a for a in neighbors if len(adj[a]) >= len(neighbors)]
            if not possible:
                return 0
            parent = min(possible, key=lambda a: len(adj[a]))
            if not (neighbors - {parent}) <= adj[parent]:
                return 0
            if len(adj[parent]) == len(neighbors):
                answer = 2
        return answer
