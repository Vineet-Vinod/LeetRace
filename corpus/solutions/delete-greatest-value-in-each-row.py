class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        rows = [sorted(row) for row in grid]
        return sum(max(row[column] for row in rows) for column in range(len(rows[0])))
