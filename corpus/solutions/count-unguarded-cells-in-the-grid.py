class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for row, col in guards:
            grid[row][col] = 1
        for row, col in walls:
            grid[row][col] = 2
        for row, col in guards:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] not in (1, 2):
                    grid[r][c] = 3
                    r += dr
                    c += dc
        return sum(cell == 0 for row in grid for cell in row)
