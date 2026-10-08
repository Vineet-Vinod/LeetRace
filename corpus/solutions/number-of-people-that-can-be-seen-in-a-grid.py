class Solution:
    def seePeople(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            stack: list[int] = []
            for col in range(cols - 1, -1, -1):
                while stack and heights[row][stack[-1]] < heights[row][col]:
                    stack.pop()
                    result[row][col] += 1
                if stack:
                    result[row][col] += 1
                stack.append(col)
        for col in range(cols):
            stack = []
            for row in range(rows - 1, -1, -1):
                while stack and heights[stack[-1]][col] < heights[row][col]:
                    stack.pop()
                    result[row][col] += 1
                if stack:
                    result[row][col] += 1
                stack.append(row)
        return result
