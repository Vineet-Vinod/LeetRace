class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        heights = [0] * len(matrix[0])
        best = 0
        for row in matrix:
            for col, value in enumerate(row):
                heights[col] = heights[col] + 1 if value else 0
            for height, width in enumerate(sorted(heights, reverse=True), 1):
                best = max(best, width * height)
        return best
