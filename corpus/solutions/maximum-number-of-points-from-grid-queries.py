from __future__ import annotations
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        import heapq

        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        answer = [0] * len(queries)
        count = 0
        for limit, index in sorted((q, i) for i, q in enumerate(queries)):
            while heap and heap[0][0] < limit:
                _, r, c = heapq.heappop(heap)
                count += 1
                for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= a < m and 0 <= b < n and (a, b) not in seen:
                        seen.add((a, b))
                        heapq.heappush(heap, (grid[a][b], a, b))
            answer[index] = count
        return answer
