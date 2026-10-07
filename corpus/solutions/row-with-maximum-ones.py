class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = max(range(len(mat)), key=lambda row: (sum(mat[row]), -row))
        return [index, sum(mat[index])]
