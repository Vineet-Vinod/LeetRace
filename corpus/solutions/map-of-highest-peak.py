from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    heights[row][col] = 0
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] == -1:
                    heights[nr][nc] = heights[row][col] + 1
                    queue.append((nr, nc))
        return heights
