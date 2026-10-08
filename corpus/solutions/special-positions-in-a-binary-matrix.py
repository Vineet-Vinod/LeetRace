class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[r][c] for r in range(len(mat))) for c in range(len(mat[0]))]
        return sum(
            mat[r][c] == 1 and row_sums[r] == 1 and col_sums[c] == 1
            for r in range(len(mat))
            for c in range(len(mat[0]))
        )
