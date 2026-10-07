class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        twos = [[0] * cols for _ in range(rows)]
        fives = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                value = grid[r][c]
                while value % 2 == 0:
                    twos[r][c] += 1
                    value //= 2
                while value % 5 == 0:
                    fives[r][c] += 1
                    value //= 5
        row2 = [[0] * (cols + 1) for _ in range(rows)]
        row5 = [[0] * (cols + 1) for _ in range(rows)]
        col2 = [[0] * cols for _ in range(rows + 1)]
        col5 = [[0] * cols for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                row2[r][c + 1] = row2[r][c] + twos[r][c]
                row5[r][c + 1] = row5[r][c] + fives[r][c]
                col2[r + 1][c] = col2[r][c] + twos[r][c]
                col5[r + 1][c] = col5[r][c] + fives[r][c]
        answer = 0
        for r in range(rows):
            for c in range(cols):
                left2, left5 = row2[r][c + 1], row5[r][c + 1]
                right2, right5 = row2[r][cols] - row2[r][c], row5[r][cols] - row5[r][c]
                up2, up5 = col2[r + 1][c], col5[r + 1][c]
                down2, down5 = col2[rows][c] - col2[r][c], col5[rows][c] - col5[r][c]
                center2, center5 = twos[r][c], fives[r][c]
                options = [
                    (left2 + up2 - center2, left5 + up5 - center5),
                    (left2 + down2 - center2, left5 + down5 - center5),
                    (right2 + up2 - center2, right5 + up5 - center5),
                    (right2 + down2 - center2, right5 + down5 - center5),
                ]
                answer = max(answer, *(min(a, b) for a, b in options))
        return answer
