class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        x_count = [0] * cols
        y_count = [0] * cols
        answer = 0
        for row in range(rows):
            row_x = row_y = 0
            for col in range(cols):
                row_x += grid[row][col] == "X"
                row_y += grid[row][col] == "Y"
                x_count[col] += row_x
                y_count[col] += row_y
                if x_count[col] == y_count[col] and x_count[col] > 0:
                    answer += 1
        return answer
