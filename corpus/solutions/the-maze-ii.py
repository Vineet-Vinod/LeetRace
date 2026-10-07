class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        rows, cols = len(maze), len(maze[0])
        distances = [[float("inf")] * cols for _ in range(rows)]
        distances[start[0]][start[1]] = 0
        queue = [(0, start[0], start[1])]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            distance, row, col = heappop(queue)
            if distance != distances[row][col]:
                continue
            if [row, col] == destination:
                return distance
            for dr, dc in directions:
                nr, nc = row, col
                steps = 0
                while (
                    0 <= nr + dr < rows
                    and 0 <= nc + dc < cols
                    and maze[nr + dr][nc + dc] == 0
                ):
                    nr += dr
                    nc += dc
                    steps += 1
                next_distance = distance + steps
                if next_distance < distances[nr][nc]:
                    distances[nr][nc] = next_distance
                    heappush(queue, (next_distance, nr, nc))
        return -1
