class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for start in range(m + n - 1):
            r = start if start < m else 0
            c = 0 if start < m else start - m + 1
            vals = []
            i, j = r, c
            while i < m and j < n:
                vals.append(mat[i][j])
                i += 1
                j += 1
            vals.sort()
            i, j = r, c
            for v in vals:
                mat[i][j] = v
                i += 1
                j += 1
        return mat
