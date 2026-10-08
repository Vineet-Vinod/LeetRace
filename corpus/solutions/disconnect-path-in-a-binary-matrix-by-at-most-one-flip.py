class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        def find_path(blocked: set[Tuple[int, int]]) -> Optional[set[Tuple[int, int]]]:
            start = (0, 0)
            goal = (rows - 1, cols - 1)
            stack = [start]
            previous = {start: None}
            while stack:
                row, col = stack.pop()
                if (row, col) == goal:
                    path = set()
                    current = goal
                    while current is not None:
                        path.add(current)
                        current = previous[current]
                    return path
                for neighbor in ((row + 1, col), (row, col + 1)):
                    nr, nc = neighbor
                    if (
                        nr < rows
                        and nc < cols
                        and grid[nr][nc]
                        and neighbor not in blocked
                        and neighbor not in previous
                    ):
                        previous[neighbor] = (row, col)
                        stack.append(neighbor)
            return None

        first_path = find_path(set())
        if first_path is None:
            return True
        internal = first_path - {(0, 0), (rows - 1, cols - 1)}
        return find_path(internal) is None
