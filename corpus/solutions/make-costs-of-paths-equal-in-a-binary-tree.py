class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        increments = 0
        for index in range(n - 1, 0, -2):
            left = cost[index - 1]
            right = cost[index]
            increments += abs(left - right)
            parent = (index - 1) // 2
            cost[parent] += max(left, right)
        return increments
