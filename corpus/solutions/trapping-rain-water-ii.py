from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        seen = [[False] * n for _ in range(m)]
        heap = []
        for r in range(m):
            for c in range(n):
                if r in (0, m - 1) or c in (0, n - 1):
                    seen[r][c] = True
                    heappush(heap, (heightMap[r][c], r, c))
        answer = 0
        while heap:
            level, r, c = heappop(heap)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n and not seen[rr][cc]:
                    seen[rr][cc] = True
                    height = heightMap[rr][cc]
                    answer += max(0, level - height)
                    heappush(heap, (max(level, height), rr, cc))
        return answer
