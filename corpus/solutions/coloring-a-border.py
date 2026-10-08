class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original = grid[row][col]
        component = {(row, col)}
        queue = deque([(row, col)])
        border: list[tuple[int, int]] = []
        while queue:
            r, c = queue.popleft()
            same = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original:
                    same += 1
                    if (nr, nc) not in component:
                        component.add((nr, nc))
                        queue.append((nr, nc))
            if same < 4:
                border.append((r, c))
        for r, c in border:
            grid[r][c] = color
        return grid
