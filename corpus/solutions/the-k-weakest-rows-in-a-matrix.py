class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = [(sum(row), index) for index, row in enumerate(mat)]
        strengths.sort()
        return [index for _, index in strengths[:k]]
