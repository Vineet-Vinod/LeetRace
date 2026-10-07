class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        heights = [0] * len(mat[0])
        answer = 0
        for row in mat:
            for col, value in enumerate(row):
                heights[col] = heights[col] + 1 if value else 0
            stack: list[tuple[int, int]] = []
            row_sum = 0
            for height in heights:
                width = 1
                while stack and stack[-1][0] >= height:
                    previous_height, previous_width = stack.pop()
                    row_sum -= previous_height * previous_width
                    width += previous_width
                stack.append((height, width))
                row_sum += height * width
                answer += row_sum
        return answer
