class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows = len(mat1)
        len(mat2)
        cols = len(mat2[0])
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for middle, value in enumerate(mat1[row]):
                if value:
                    for col, right in enumerate(mat2[middle]):
                        if right:
                            result[row][col] += value * right
        return result
