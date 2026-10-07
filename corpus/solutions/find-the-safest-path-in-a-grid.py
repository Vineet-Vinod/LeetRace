class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        size = len(grid)
        distance = [[-1] * size for _ in range(size)]
        queue = deque()
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 1:
                    distance[row][col] = 0
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    0 <= next_row < size
                    and 0 <= next_col < size
                    and distance[next_row][next_col] == -1
                ):
                    distance[next_row][next_col] = distance[row][col] + 1
                    queue.append((next_row, next_col))
        safest = [[-1] * size for _ in range(size)]
        safest[0][0] = distance[0][0]
        queue = [(-distance[0][0], 0, 0)]
        while queue:
            negative, row, col = heappop(queue)
            value = -negative
            if value < safest[row][col]:
                continue
            if row == size - 1 and col == size - 1:
                return value
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if 0 <= next_row < size and 0 <= next_col < size:
                    candidate = min(value, distance[next_row][next_col])
                    if candidate > safest[next_row][next_col]:
                        safest[next_row][next_col] = candidate
                        heappush(queue, (-candidate, next_row, next_col))
        return safest[-1][-1]
