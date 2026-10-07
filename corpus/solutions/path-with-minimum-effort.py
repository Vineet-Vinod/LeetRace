class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[inf] * cols for _ in range(rows)]
        effort[0][0] = 0
        queue = [(0, 0, 0)]
        while queue:
            current, row, col = heappop(queue)
            if (row, col) == (rows - 1, cols - 1):
                return current
            if current != effort[row][col]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    candidate = max(current, abs(heights[row][col] - heights[nr][nc]))
                    if candidate < effort[nr][nc]:
                        effort[nr][nc] = candidate
                        heappush(queue, (candidate, nr, nc))
        return 0
