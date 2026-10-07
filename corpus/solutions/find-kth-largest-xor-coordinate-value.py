class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows, columns = len(matrix), len(matrix[0])
        values = []
        prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                prefix[row][column] = (
                    matrix[row - 1][column - 1]
                    ^ prefix[row - 1][column]
                    ^ prefix[row][column - 1]
                    ^ prefix[row - 1][column - 1]
                )
                values.append(prefix[row][column])
        values.sort(reverse=True)
        return values[k - 1]
