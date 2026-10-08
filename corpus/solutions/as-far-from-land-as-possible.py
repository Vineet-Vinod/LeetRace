class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()
        water = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    queue.append((r, c))
                else:
                    water += 1
        if water == 0 or water == n * n:
            return -1
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))
        return max(max(row) for row in distance)
