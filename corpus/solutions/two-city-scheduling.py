class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ordered = sorted(costs, key=lambda pair: pair[0] - pair[1])
        half = len(costs) // 2
        return sum(pair[0] for pair in ordered[:half]) + sum(
            pair[1] for pair in ordered[half:]
        )
