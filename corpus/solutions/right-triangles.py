class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row_counts = [sum(row) for row in grid]
        col_counts = [
            sum(grid[row][col] for row in range(len(grid)))
            for col in range(len(grid[0]))
        ]
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    answer += (row_counts[row] - 1) * (col_counts[col] - 1)
        return answer
