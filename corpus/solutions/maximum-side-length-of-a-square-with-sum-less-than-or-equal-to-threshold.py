class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                prefix[row + 1][col + 1] = (
                    mat[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col]
                )
        best = 0
        for top in range(rows):
            for left in range(cols):
                maximum = min(rows - top, cols - left)
                for side in range(best + 1, maximum + 1):
                    bottom, right = top + side, left + side
                    total = (
                        prefix[bottom][right]
                        - prefix[top][right]
                        - prefix[bottom][left]
                        + prefix[top][left]
                    )
                    if total <= threshold:
                        best = side
                    else:
                        break
        return best
