class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_row, start_col = entrance
        queue = deque([(start_row, start_col, 0)])
        seen = {(start_row, start_col)}
        while queue:
            row, col, distance = queue.popleft()
            if distance and (row in (0, rows - 1) or col in (0, cols - 1)):
                return distance
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and maze[next_row][next_col] == "."
                    and (next_row, next_col) not in seen
                ):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, distance + 1))
        return -1
