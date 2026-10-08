class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(value % 2 == 0 for value in position)
        return min(even, len(position) - even)
