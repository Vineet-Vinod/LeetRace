class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {value: rank for rank, value in enumerate(sorted(set(arr)), 1)}
        return [ranks[value] for value in arr]
