class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for _ in range(query_row):
            next_row = [0.0] * (len(row) + 1)
            for index, amount in enumerate(row):
                excess = max(0.0, amount - 1.0) / 2.0
                next_row[index] += excess
                next_row[index + 1] += excess
            row = next_row
        return min(1.0, row[query_glass])
