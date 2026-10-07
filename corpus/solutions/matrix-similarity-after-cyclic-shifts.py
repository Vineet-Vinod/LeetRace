class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        _rows, cols = len(mat), len(mat[0])
        shift = k % cols
        for row_index, row in enumerate(mat):
            if row_index % 2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[-shift:] + row[:-shift] if shift else row[:]
            if shifted != row:
                return False
        return True
