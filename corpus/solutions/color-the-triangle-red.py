class Solution:
    def colorRed(self, n: int) -> list[list[int]]:
        result = [[1, 1]]
        for row in range(2, n + 1):
            phase = (n - row) % 4
            if phase == 0:
                columns = range(1, 2 * row, 2)
            elif phase == 1:
                columns = range(2, 3)
            elif phase == 2:
                columns = range(3, 2 * row, 2)
            else:
                columns = range(1, 2)
            result.extend([row, col] for col in columns)
        return result
