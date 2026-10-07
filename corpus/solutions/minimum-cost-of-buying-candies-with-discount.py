class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ordered = sorted(cost, reverse=True)
        return sum(value for index, value in enumerate(ordered) if index % 3 != 2)
