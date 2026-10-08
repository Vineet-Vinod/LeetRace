class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for row in range(rows):
            for col in (0, cols - 1):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))
        for col in range(cols):
            for row in (0, rows - 1):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for nr, nc in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
        return sum(map(sum, grid))
