class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        low, high = pricing
        queue = deque([(start[0], start[1], 0)])
        seen = {(start[0], start[1])}
        ranked = []
        while queue:
            row, col, distance = queue.popleft()
            price = grid[row][col]
            if low <= price <= high and price > 1:
                ranked.append((distance, price, row, col))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] != 0
                    and (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, distance + 1))
        ranked.sort()
        return [[row, col] for _, _, row, col in ranked[:k]]
