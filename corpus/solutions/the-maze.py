class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        rows, cols = len(maze), len(maze[0])
        queue = deque([tuple(start)])
        visited = {tuple(start)}
        while queue:
            row, col = queue.popleft()
            if [row, col] == destination:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row, col
                while (
                    0 <= nr + dr < rows
                    and 0 <= nc + dc < cols
                    and maze[nr + dr][nc + dc] == 0
                ):
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False
