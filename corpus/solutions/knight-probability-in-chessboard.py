class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
        probabilities = [[0.0] * n for _ in range(n)]
        probabilities[row][column] = 1.0
        for _ in range(k):
            next_probabilities = [[0.0] * n for _ in range(n)]
            for current_row in range(n):
                for current_col in range(n):
                    chance = probabilities[current_row][current_col] / 8.0
                    if chance == 0:
                        continue
                    for dr, dc in moves:
                        next_row, next_col = current_row + dr, current_col + dc
                        if 0 <= next_row < n and 0 <= next_col < n:
                            next_probabilities[next_row][next_col] += chance
            probabilities = next_probabilities
        return sum(map(sum, probabilities))
