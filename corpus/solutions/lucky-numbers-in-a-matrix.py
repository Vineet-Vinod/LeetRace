class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        column_maxima = [max(column) for column in zip(*matrix)]
        result = [min(row) for row in matrix if min(row) in column_maxima]
        return sorted(result)
