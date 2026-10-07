from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        distance = [[10**20] * cols for _ in grid]
        distance[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if time != distance[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return time
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    arrival = time + 1
                    if arrival < grid[nr][nc]:
                        arrival = grid[nr][nc] + (grid[nr][nc] - arrival) % 2
                    if arrival < distance[nr][nc]:
                        distance[nr][nc] = arrival
                        heapq.heappush(heap, (arrival, nr, nc))
        return -1
