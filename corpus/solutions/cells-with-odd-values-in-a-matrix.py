class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0] * m
        columns = [0] * n
        for row, column in indices:
            rows[row] += 1
            columns[column] += 1
        return sum(
            (rows[row] + columns[column]) % 2 for row in range(m) for column in range(n)
        )
