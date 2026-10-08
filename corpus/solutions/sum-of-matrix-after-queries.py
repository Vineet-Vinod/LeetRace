class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen_rows = set()
        seen_cols = set()
        rows_left = cols_left = n
        total = 0
        for kind, index, value in reversed(queries):
            if kind == 0 and index not in seen_rows:
                total += value * cols_left
                seen_rows.add(index)
                rows_left -= 1
            elif kind == 1 and index not in seen_cols:
                total += value * rows_left
                seen_cols.add(index)
                cols_left -= 1
        return total
