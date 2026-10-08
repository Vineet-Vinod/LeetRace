class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        best = 0
        for row in matrix:
            for j, x in enumerate(row):
                heights[j] = heights[j] + 1 if x == "1" else 0
            stack = [-1]
            for j, h in enumerate(heights):
                while stack[-1] != -1 and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    best = max(best, height * (j - stack[-1] - 1))
                stack.append(j)
        return best
