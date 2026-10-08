from collections import deque
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        remaining = [0] * n
        for p in parent[1:]:
            remaining[p] += 1
        best = [[0, 0] for _ in parent]
        queue = deque(i for i in range(n) if remaining[i] == 0)
        answer = 1
        while queue:
            node = queue.popleft()
            answer = max(answer, 1 + sum(best[node]))
            p = parent[node]
            if p != -1:
                if s[p] != s[node]:
                    length = 1 + best[node][0]
                    if length >= best[p][0]:
                        best[p] = [length, best[p][0]]
                    elif length > best[p][1]:
                        best[p][1] = length
                remaining[p] -= 1
                if remaining[p] == 0:
                    queue.append(p)
        return answer
