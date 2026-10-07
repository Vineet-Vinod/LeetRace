class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        total = sum(mat[i][i] + mat[i][size - 1 - i] for i in range(size))
        if size % 2:
            total -= mat[size // 2][size // 2]
        return total
