class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = grid[0][0]
        heap = [(-grid[0][0], 0, 0)]
        while heap:
            negative_score, row, col = heappop(heap)
            score = -negative_score
            if score < best[row][col]:
                continue
            if row == rows - 1 and col == cols - 1:
                return score
            for nr, nc in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= nr < rows and 0 <= nc < cols:
                    candidate = min(score, grid[nr][nc])
                    if candidate > best[nr][nc]:
                        best[nr][nc] = candidate
                        heappush(heap, (-candidate, nr, nc))
        return -1
