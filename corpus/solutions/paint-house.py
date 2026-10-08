class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        a, b, c = costs[0]
        for x, y, z in costs[1:]:
            a, b, c = x + min(b, c), y + min(a, c), z + min(a, b)
        return min(a, b, c)
