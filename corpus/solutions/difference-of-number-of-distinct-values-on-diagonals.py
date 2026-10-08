class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        answer = [[0] * cols for _ in range(rows)]
        for start_row in range(rows):
            for start_col in range(cols):
                above: set[int] = set()
                r, c = start_row - 1, start_col - 1
                while r >= 0 and c >= 0:
                    above.add(grid[r][c])
                    r -= 1
                    c -= 1
                below: set[int] = set()
                r, c = start_row + 1, start_col + 1
                while r < rows and c < cols:
                    below.add(grid[r][c])
                    r += 1
                    c += 1
                answer[start_row][start_col] = abs(len(above) - len(below))
        return answer
