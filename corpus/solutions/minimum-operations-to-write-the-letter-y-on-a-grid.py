class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y_counts = [0, 0, 0]
        other_counts = [0, 0, 0]
        y_total = other_total = 0
        center = n // 2
        for r in range(n):
            for c in range(n):
                is_y = (r <= center and (c == r or c == n - 1 - r)) or (
                    r > center and c == center
                )
                if is_y:
                    y_counts[grid[r][c]] += 1
                    y_total += 1
                else:
                    other_counts[grid[r][c]] += 1
                    other_total += 1
        answer = n * n
        for y_color in range(3):
            for other_color in range(3):
                if y_color != other_color:
                    answer = min(
                        answer,
                        y_total
                        - y_counts[y_color]
                        + other_total
                        - other_counts[other_color],
                    )
        return answer
