class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        values = [value for row in mat for value in row]
        if len(values) != r * c:
            return mat
        return [values[start : start + c] for start in range(0, len(values), c)]
