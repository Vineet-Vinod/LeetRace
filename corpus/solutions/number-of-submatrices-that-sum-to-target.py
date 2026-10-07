from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        if len(matrix) > len(matrix[0]):
            matrix = [list(row) for row in zip(*matrix)]
        m, n = len(matrix), len(matrix[0])
        result = 0
        for top in range(m):
            columns = [0] * n
            for bottom in range(top, m):
                seen: dict[int, int] = defaultdict(int)
                seen[0] = 1
                running = 0
                for j in range(n):
                    columns[j] += matrix[bottom][j]
                    running += columns[j]
                    result += seen[running - target]
                    seen[running] += 1
        return result
