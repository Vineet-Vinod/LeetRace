from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        groups = defaultdict(list)
        for r in range(m):
            for c in range(n):
                groups[mat[r][c]].append((r, c))
        rows, columns = [0] * m, [0] * n
        for value in sorted(groups):
            updates = [(r, c, 1 + max(rows[r], columns[c])) for r, c in groups[value]]
            for r, c, length in updates:
                rows[r] = max(rows[r], length)
                columns[c] = max(columns[c], length)
        return max(rows)
