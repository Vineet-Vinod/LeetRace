class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common = set(mat[0])
        for row in mat[1:]:
            common.intersection_update(row)
            if not common:
                return -1
        return min(common) if common else -1
