class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_steps_back = 0
        one_step_back = 0
        for index in range(2, len(cost) + 1):
            current = min(
                one_step_back + cost[index - 1], two_steps_back + cost[index - 2]
            )
            two_steps_back, one_step_back = one_step_back, current
        return one_step_back
