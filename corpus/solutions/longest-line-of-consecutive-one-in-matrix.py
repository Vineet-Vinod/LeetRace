class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        vertical = [0] * cols
        diagonal = [0] * cols
        anti_diagonal = [0] * cols
        best = 0
        for row in range(rows):
            previous_diagonal = diagonal.copy()
            previous_anti = anti_diagonal.copy()
            horizontal = 0
            for col in range(cols):
                if mat[row][col] == 0:
                    horizontal = vertical[col] = diagonal[col] = anti_diagonal[col] = 0
                    continue
                horizontal += 1
                vertical[col] += 1
                diagonal[col] = 1 + (previous_diagonal[col - 1] if col else 0)
                anti_diagonal[col] = 1 + (
                    previous_anti[col + 1] if col + 1 < cols else 0
                )
                best = max(
                    best, horizontal, vertical[col], diagonal[col], anti_diagonal[col]
                )
        return best
