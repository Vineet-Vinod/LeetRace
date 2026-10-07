from typing import List
from collections import deque


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        result = [[[0, 0] for c in range(n)] for m in range(n)]
        degree = [
            [[len(graph[m]), sum(v != 0 for v in graph[c])] for c in range(n)]
            for m in range(n)
        ]
        q = deque()
        for c in range(1, n):
            for t in range(2):
                result[0][c][t] = 1
                q.append((0, c, t, 1))
                result[c][c][t] = 2
                q.append((c, c, t, 2))
        while q:
            m, c, t, w = q.popleft()
            parents = (
                ((pm, c, 0) for pm in graph[m])
                if t == 1
                else ((m, pc, 1) for pc in graph[c] if pc != 0)
            )
            for pm, pc, pt in parents:
                if result[pm][pc][pt]:
                    continue
                degree[pm][pc][pt] -= 1
                if w == pt + 1 or degree[pm][pc][pt] == 0:
                    result[pm][pc][pt] = w
                    q.append((pm, pc, pt, w))
        return result[1][2][0]
